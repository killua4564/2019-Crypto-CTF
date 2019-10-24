import string
import hashlib
import itertools
from pwn import *

conn = remote("167.71.62.250", "20029")

def pow():
	conn.recvuntil("such that ")
	hashfunc = conn.recvuntil("(X)").replace(b"(X)", b"").decode()
	conn.recvuntil(" = ")
	tailhash = conn.recvuntil("\n").strip(b"\n").decode()

	if 'md5' == hashfunc: func = hashlib.md5 
	elif 'sha1' == hashfunc: func = hashlib.sha1
	elif 'sha224' == hashfunc: func = hashlib.sha224
	elif 'sha256' == hashfunc: func = hashlib.sha256
	elif 'sha384' == hashfunc: func = hashlib.sha384
	elif 'sha512' == hashfunc: func = hashlib.sha512

	for length in range(1, 10):
		for x in itertools.product(string.digits + string.ascii_lowercase + string.ascii_uppercase, repeat=length):
			h = func(''.join(x).encode()).hexdigest()
			if h[-6:] == tailhash:
				conn.sendline(''.join(x))
				return

# [S]how encrypted msgs!
# g                  = (24, 31, 12, 25, 4, 36, 32, 9, 29, 39, 7, 34, 5, 2, 11, 30, 15, 3, 21, 35, 17, 19, 23, 33, 8, 22, 16, 13, 10, 20, 1, 38, 28, 26, 6, 40, 14, 27, 18, 37)
# key * g * key^(-1) = (4, 25, 18, 2, 33, 6, 32, 40, 14, 36, 23, 39, 3, 38, 22, 31, 9, 12, 8, 21, 29, 10, 1, 13, 5, 27, 35, 19, 11, 15, 26, 20, 17, 24, 28, 34, 16, 37, 7, 30)
# g                  = (30, 11, 38, 19, 18, 22, 29, 2, 20, 34, 23, 3, 27, 33, 24, 4, 39, 7, 10, 12, 15, 5, 6, 25, 14, 32, 13, 40, 26, 17, 16, 31, 36, 37, 9, 21, 8, 28, 1, 35)
# key * g * key^(-1) = (8, 13, 32, 6, 30, 37, 39, 36, 23, 29, 1, 2, 20, 7, 33, 11, 10, 19, 9, 25, 22, 12, 18, 14, 28, 34, 40, 17, 3, 31, 38, 26, 15, 35, 4, 27, 21, 24, 5, 16)
# g                  = (6, 11, 21, 33, 32, 40, 35, 10, 29, 27, 13, 2, 7, 17, 20, 16, 28, 24, 36, 12, 15, 26, 14, 19, 25, 38, 23, 37, 22, 8, 5, 4, 34, 30, 3, 9, 1, 18, 39, 31)
# key * g * key^(-1) = (14, 38, 33, 15, 12, 27, 35, 29, 34, 40, 1, 8, 21, 7, 2, 24, 17, 18, 37, 5, 20, 25, 30, 13, 10, 19, 23, 22, 16, 26, 28, 9, 6, 3, 4, 36, 31, 39, 11, 32)
# g                  = (7, 24, 25, 31, 21, 30, 14, 22, 1, 20, 6, 29, 16, 36, 19, 40, 13, 5, 4, 18, 15, 17, 27, 34, 37, 33, 10, 38, 3, 9, 2, 11, 8, 12, 28, 26, 35, 39, 32, 23)
# key * g * key^(-1) = (29, 27, 14, 37, 18, 33, 13, 32, 24, 28, 1, 22, 39, 12, 17, 20, 31, 25, 2, 40, 23, 11, 15, 19, 4, 38, 16, 35, 10, 5, 6, 7, 3, 21, 8, 26, 9, 30, 36, 34)
# g                  = (5, 12, 36, 14, 8, 25, 40, 1, 39, 21, 15, 26, 32, 20, 13, 33, 37, 30, 27, 22, 31, 10, 3, 9, 17, 35, 16, 38, 23, 29, 6, 18, 11, 24, 4, 2, 28, 19, 7, 34)
# key * g * key^(-1) = (15, 31, 11, 1, 29, 39, 20, 24, 13, 27, 28, 9, 6, 21, 25, 35, 40, 2, 22, 38, 3, 34, 26, 18, 12, 30, 14, 37, 33, 5, 32, 8, 17, 19, 7, 23, 36, 10, 16, 4)
# g                  = (10, 30, 6, 12, 22, 25, 20, 3, 8, 24, 9, 19, 14, 7, 4, 17, 1, 21, 36, 31, 23, 11, 28, 15, 16, 40, 39, 38, 32, 37, 13, 2, 29, 18, 27, 5, 35, 33, 26, 34)
# key * g * key^(-1) = (10, 14, 8, 24, 40, 30, 29, 1, 26, 7, 6, 11, 25, 28, 27, 22, 23, 20, 3, 31, 4, 21, 19, 34, 35, 38, 2, 15, 16, 5, 32, 12, 18, 39, 9, 17, 36, 33, 37, 13)
# g                  = (25, 33, 1, 13, 17, 11, 23, 19, 37, 12, 10, 39, 4, 14, 38, 36, 5, 32, 34, 7, 15, 18, 27, 29, 22, 2, 6, 24, 28, 40, 35, 21, 31, 30, 9, 16, 8, 20, 26, 3)
# key * g * key^(-1) = (5, 6, 7, 3, 14, 33, 18, 13, 31, 15, 1, 25, 30, 2, 10, 17, 16, 20, 36, 35, 12, 23, 22, 26, 11, 34, 27, 38, 32, 8, 39, 9, 37, 29, 40, 21, 4, 24, 19, 28)
# g                  = (17, 18, 14, 6, 29, 39, 3, 15, 26, 30, 25, 21, 36, 20, 5, 13, 11, 32, 4, 23, 12, 7, 2, 9, 24, 33, 10, 31, 27, 40, 1, 8, 38, 34, 28, 37, 16, 22, 35, 19)
# key * g * key^(-1) = (22, 39, 9, 36, 21, 35, 11, 24, 31, 37, 7, 25, 33, 6, 16, 26, 15, 38, 23, 40, 2, 13, 4, 20, 34, 17, 14, 19, 10, 28, 29, 32, 3, 1, 12, 8, 18, 30, 27, 5)
# g                  = (2, 37, 7, 10, 11, 33, 19, 16, 32, 9, 28, 29, 23, 14, 3, 25, 38, 24, 20, 36, 6, 1, 34, 8, 40, 31, 5, 17, 13, 27, 4, 35, 18, 30, 12, 15, 21, 22, 26, 39)
# key * g * key^(-1) = (39, 29, 24, 30, 21, 32, 13, 34, 33, 3, 37, 8, 15, 16, 6, 1, 36, 20, 35, 28, 19, 4, 5, 25, 38, 11, 27, 10, 14, 23, 18, 9, 22, 17, 26, 31, 40, 7, 2, 12)
# g                  = (9, 30, 14, 6, 16, 25, 28, 11, 31, 1, 4, 15, 27, 37, 12, 18, 32, 26, 13, 22, 38, 10, 5, 23, 29, 33, 36, 39, 2, 24, 8, 3, 40, 19, 7, 34, 17, 35, 20, 21)
# key * g * key^(-1) = (7, 30, 19, 10, 38, 22, 1, 6, 8, 37, 5, 20, 35, 21, 33, 32, 12, 14, 24, 40, 3, 17, 25, 28, 39, 23, 26, 34, 15, 18, 11, 29, 16, 4, 9, 13, 36, 2, 27, 31)
# | please send M to see another part of encrypted msgs!!

# [G]uess the key       
# [E]ncryption function 

def gen_divan(l, n):
    assert l < n**2
    key, F = random_permutation(n), []
    for _ in range(l):
        g = random_permutation(n)
        F.append((str(g.to_image()), str((key * g * key.inverse()).to_image())))
    return key, F

if __name__ == '__main__':
	pow()
	conn.interactive()