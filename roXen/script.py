from sympy import invert, root, gcd
from Crypto.Util.number import *

n = 0x3ff77ad8783e006b6a2c9857f2f13a9d896297558e7c986c491e30c1a920512a0bad9f07c5569cf998fc35a3071de9d8b0f5ada4f8767b828e35044abce5dcf88f80d1c0a0b682605cce776a184e1bcb8118790fff92dc519d24f998a9c04faf43c434bef6c0fa39a3db7452dc07ccfced9271799f37d91d56b5f21c51651d6a9a41ee5a8af17a2f945fac2b1a0ea98bc70ef0f3e37371c9c7b6f90d3d811212fc80e0abcd5bbefe0c6edb3ca6845ded90677ccd8ff4de2c747b37265fc1250ba9aa89b4fd2bdfb4b4b72a7ff5b5ee67e81fd25027b6cb49db610ec60a05016e125ce0848f2c32bff33eed415a6d227262b338b0d1f3803d83977341c0d3638f
ct = 0x2672cade2272f3024fd2d1984ea1b8e54809977e7a8c70a07e2560f39e6fcce0e292426e28df51492dec67d000d640f3e5b4c6c447845e70d1432a3c816a33da6a276b0baabd0111279c9f267a90333625425b1d73f1cdc254ded2ad54955914824fc99e65b3dea3e365cfb1dce6e025986b2485b6c13ca0ee73c2433cf0ca0265afe42cbf647b5c721a6e51514220bab8fcb9cff570a6922bceb12e9d61115357afe1705bda3c3f0b647ba37711c560b75841135198cc076d0a52c74f9802760c1f881887cc3e50b7e0ff36f0d9fa1bfc66dff717f032c066b555e315cb07e3df13774eaa70b18ea1bb3ea0fd1227d4bac84be2660552d3885c79815baef661

'''
44 + adlit(44) = 63
120 + adlit(120) = 127

so
p + adlit(p) = 2**1024 - 1
q = 2**1024 - p + 31336
n = p * (2**1024 - p + 31336)
p**2 - (2**1024 + 31336)p + n = 0
'''

a = 1
b = -(2**1024 + 31336)
c = n
d = int(root(b ** 2 - 4 * a * c, 2))
p = (-b + d) // (2 * a)
q = n // p

assert isPrime(p) and isPrime(q)
assert p * q == n

'''
for ei in range(4096):
	try:
		g = gcd(2 ** ei - 1, (p-1) * (q-1))
		d = int(invert((2 ** ei - 1) // g, (p-1) * (q-1)))
		flag = long_to_bytes(pow(pow(ct, d, n), 1 / g))
		if b"CCTF" in flag:
			print(ei)
			print(flag)
			break
	except:
		print(ei)
'''

ei = 3729
g = gcd(2 ** ei - 1, (p-1) * (q-1))
d = int(invert((2 ** ei - 1) // g, (p-1) * (q-1)))
flag = long_to_bytes(int(root(pow(ct, d, n), g)))
print(flag.decode())
