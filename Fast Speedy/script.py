from Crypto.Util.number import *

def drift(R, B):
	n = len(B)
	ans, ini = R[-1], 0
	for i in B:
		ini ^= R[i-1]
	R = [ini] + R[:-1]
	return ans, R, ini

flag = open('flag.png.enc', 'rb').read()
flag = bin(bytes_to_long(flag))[2:].zfill(len(flag) * 8)
png = bin(bytes_to_long(open('fake.png','rb').read()[:16]))[2:]
R = [int(i) ^ int(j) for i, j in zip(flag, png)]

a = []
for r in range(7, len(R)):
	for s in range(2, r):
		key = True
		B = range(s)
		RR, RT = R[:r][::-1], R[r:]
		for rt in RT:
			_, RR, t = drift(RR, B)
			if t != rt:
				key = False
				break
		if key:
			a.append((r, s))

for r, s in a:
	RR = R[:r][::-1]
	B = range(s)
	dec = []
	for i in range(len(flag)):
		ans, RR, _ = drift(RR, B)
		dec = dec + [int(flag[i]) ^ ans]

	dec = ''.join([str(b) for b in dec])
	open("flag_{}_{}.png".format(str(r), str(s)), "wb").write(long_to_bytes(int(dec, 2)))