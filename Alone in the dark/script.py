from gmpy import next_prime
from gmpy2 import iroot, is_prime

'''
2 * u ** 2 + 2 * u + 1 == v ** 2
3 * x ** 2 + 3 * x + 1 == y ** 2

(v-1) * (v+1) = 2 * u * (u+1)
(y-1) * (y+1) = 3 * x * (x+1)
'''

u = 1 << 664 - 1
v = int(iroot(2 * u * (u + 1) + 1, 2)[0])
while True:
	v = int(next_prime(v))
	u = int(iroot((v ** 2 - 1) // 2, 2)[0])
	if 2 * u * (u + 1) + 1 == v ** 2:
		break

print(u)
print(v)

x = 1 << 600 - 1
y = int(iroot(3 * x * (x + 1) + 1, 2)[0])
while True:
	y = int(next_prime(y))
	x = int(iroot((y ** 2 - 1) // 3, 2)[0])
	if 3 * x * (x + 1) + 1 == y ** 2:
		break

print(x)
print(y)

from hashlib import sha256
print(f'CCTF{{{sha256((str(u) + str(v) + str(x) + str(y)).encode()).hexdigest()}}}')