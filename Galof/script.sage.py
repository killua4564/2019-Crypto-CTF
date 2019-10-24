
# This file was *autogenerated* from the file script.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_255 = Integer(255); _sage_const_256 = Integer(256); _sage_const_64 = Integer(64); _sage_const_16 = Integer(16); _sage_const_199 = Integer(199)
import binascii
F = GF(_sage_const_2 )['x']; (x,) = F._first_ngens(1)
base = x**_sage_const_255  + x**_sage_const_199  + _sage_const_1 

r1 = "uXu2FTYWpCWSXcPwpv4mc0V8nhl2T7"
r2 = "PBFnf2mSWiHUNxMr90KJC6TubsKjU9"
enc1 = "582c7d41f27a92ad373dec06175f8b0d399bc5d858253bb4b6530c6c608992b1"
enc2 = "186f2f1f0eeab93e621b34dbc1fa515b5b74fc761afb9e74a560598844ab9160"

r1 = sum([int(v) * x**i for i, v in enumerate(bin(int(r1.encode('hex'), _sage_const_16 ))[_sage_const_2 :][::-_sage_const_1 ])])
r2 = sum([int(v) * x**i for i, v in enumerate(bin(int(r2.encode('hex'), _sage_const_16 ))[_sage_const_2 :][::-_sage_const_1 ])])
enc1 = sum([int(v) * x**i for i, v in enumerate(bin(int(enc1, _sage_const_16 ))[_sage_const_2 :][::-_sage_const_1 ])])
enc2 = sum([int(v) * x**i for i, v in enumerate(bin(int(enc2, _sage_const_16 ))[_sage_const_2 :][::-_sage_const_1 ])])

key1 = ((enc1 - enc2) * r1 * r2 * inverse_mod(r1 + r2, base)) % base
key2 = (enc1 - key1 * inverse_mod(r1, base)) % base

flag = "46c5c88ef8c8f6d49ffc763d56e9cd33176d9aa14c039281d506b834d48c1066"
flag = sum([int(v) * x**i for i, v in enumerate(bin(int(flag, _sage_const_16 ))[_sage_const_2 :][::-_sage_const_1 ])])
flag = inverse_mod(((flag - key2) * inverse_mod(key1, base)) % base, base)

dec = ''
EXP = flag.exponents()
for i in range(_sage_const_256 ):
	if i in EXP:
		dec += '1'
	else:
		dec += '0'
dec = hex(int(dec[::-_sage_const_1 ], _sage_const_2 )).lstrip('0x').rstrip('L').zfill(_sage_const_64 )
print(binascii.unhexlify(dec))

