import string
import hashlib
import itertools
from pwn import *

conn = remote("167.71.62.250", "12439")

def proof():
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

# *********************************************************************************
# | hey! I have developed an efficient pseudorandom function, PRF, but it needs   |
# | deep tests for security points!! Try hard to break this PRF and get the flag! |
# | In each step I will compute the f_a(n), f_a(n + 1), f_a(n + 2), f_a(n+3), and |
# | f_a(n + 4) for secret verctor a, and for your given positive number 0 < n < p |
# *********************************************************************************
# | for n = 133158862344346590334397918372612285427, and with these PRF parameters: 
# | (p, g) = (0x914f509fb70ae8185bb1b6660e3d8825, 0x68cd36c08d416e66e3d11efece9da5e2) 
# | the five consecutive random numbers generated by our secure PRF are: 
# | f_a(n + 0) = 173185049728365488750339379526359753025
# | f_a(n + 1) = 121522206766834964664059167127277094952
# | f_a(n + 2) = 17978839874240986103119721600783001582
# | f_a(n + 3) = 139711204017094569001743185245125418963
# | f_a(n + 4) = 94580224642423863484518869705711364857 
# | Options: 
# |    [G]uess next number! 
# |    [P]RF function 
# |    [N]ew numbers
# |    [Q]uit

def gg(tup, a, x):
    (_, p, g), n = tup, len(a)
    assert len(bin(x)[2:]) <= n
    X = bin(x)[2:].zfill(n)
    f_ax = g
    for i in range(1, n):
        f_ax *= pow(g, a[i] * int(X[i]), p)
    return f_ax % p

if __name__ == '__main__':
	proof()
	conn.interactive()