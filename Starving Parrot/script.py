import string
import hashlib
import itertools
from pwn import *

conn = remote("167.71.62.250", "43139")

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

# |-------------------------------------|
# | Options:                            |
# |    [E]ncryption function         |
# |    [K]eygen function             |
# |    [O]racle function             |
# |    [F]lag (encrypted)!           |
# |    [P]ublic key!                 |
# |    [T]est poracle                |
# |    [Q]uit                        |
# |-------------------------------------|

def encrypt(n, msg):
    msg = bytes_to_long(msg)
    assert 8 * msg < n
    msg *= 2
    msg += 1
    enc = msg
    enc %= n
    return ((jacobi(msg, n) + 3) * enc) ** 2 % n

def keygen(nbit): # non-performant and dirty function
    while True:
        r, s = random.getrandbits(nbit), random.getrandbits(nbit)
        p, q = poracle(r), poracle(s)
        if isPrime(p):
            if isPrime(q):
                if p % 8 == 3:
                    n = p * q
                    if n % 8 == 5:
                        return n

def poracle(r):
    if r >= 2**40:
        return poly(r) # secret polynomial
    else:
        u = random.randint(1, 2**40)
        return poly(u * r)

# | the encrypted flag is: 2359703796038663587597468057074132729719274350813052854273779099014127612050044398871693557711797805699866160239924300268952844316671084082652612804046369997301400867931193888766181555513443057601278492427222046174586601802018748529733905859005513893632016357442287925172387553714771862914038177792117770080423925013463887874822980263257344539666958930019078099191705525685490313237039613920923424073855037369131139466164
# | the public key is n = 16502777433805863390167368741524364988778697629031915368037694171300902768201377770492539759346559649932942260776502886707515670884338283566826100395693507310255016103890967238161804431369425551705361901376583566840800362085929439639779453399912568489712642012702566537020811966619670927878284556136667530175354652490355773576346637754612281607893692375105022143316497678874193485568203255632674090320122681678065612564317
# | send an integer: 
# | poracle(1233) = 33580594092122104726309108808769865499183085684389030615882230910636477274452218994165995297998080918132022649083967918417578676606411069202340857358940466575147490783582331907827980726409468625389

if __name__ == '__main__':
	proof()

	conn.interactive()