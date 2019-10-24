import binascii
F.<x> = GF(2)[]
base = x^255 + x^199 + 1

r1 = "uXu2FTYWpCWSXcPwpv4mc0V8nhl2T7"
r2 = "PBFnf2mSWiHUNxMr90KJC6TubsKjU9"
enc1 = "582c7d41f27a92ad373dec06175f8b0d399bc5d858253bb4b6530c6c608992b1"
enc2 = "186f2f1f0eeab93e621b34dbc1fa515b5b74fc761afb9e74a560598844ab9160"

r1 = sum([int(v) * x^i for i, v in enumerate(bin(int(r1.encode('hex'), 16))[2:][::-1])])
r2 = sum([int(v) * x^i for i, v in enumerate(bin(int(r2.encode('hex'), 16))[2:][::-1])])
enc1 = sum([int(v) * x^i for i, v in enumerate(bin(int(enc1, 16))[2:][::-1])])
enc2 = sum([int(v) * x^i for i, v in enumerate(bin(int(enc2, 16))[2:][::-1])])

key1 = ((enc1 - enc2) * r1 * r2 * inverse_mod(r1 + r2, base)) % base
key2 = (enc1 - key1 * inverse_mod(r1, base)) % base

flag = "46c5c88ef8c8f6d49ffc763d56e9cd33176d9aa14c039281d506b834d48c1066"
flag = sum([int(v) * x^i for i, v in enumerate(bin(int(flag, 16))[2:][::-1])])
flag = inverse_mod(((flag - key2) * inverse_mod(key1, base)) % base, base)

dec = ''
EXP = flag.exponents()
for i in range(256):
	if i in EXP:
		dec += '1'
	else:
		dec += '0'
dec = hex(int(dec[::-1], 2)).lstrip('0x').rstrip('L').zfill(64)
print(binascii.unhexlify(dec))