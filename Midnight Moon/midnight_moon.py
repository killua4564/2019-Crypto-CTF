#!/usr/bin/env python

from Crypto.Util.number import *
from fractions import gcd
import random
from flag import flag


def encrypt(msg):
    l = len(msg) // 2
    k, m = bytes_to_long(msg[:l]), bytes_to_long(msg[l:])
    c = 0
    A = []
    while c < 2:
        if isPrime(m):
            A.append(m)
            m <<= 1
            m +=  1
            c +=  1
        else:
            m *= l
            m += l
            m ^= l
    p, q = A
    n = p * q
    s = 3
    while True:
        t = (p - 1) / 2
        while t % 2 == 0:
            t /= 2
        if t % s == 0:
            r = t / s
            if t % (r**2) != 0:
                if gcd(r, q - 1) == 1:
                    break
        s += 2
    while True:
        y = random.randint(1, n)
        if pow(y, (p - 1) * (q - 1) / r, n) != 1:
            break
    while True:
        u, v = random.randint(1, n), random.randint(1, n)
        if gcd(u, n) * gcd(v, n) == 1:
            break
    C = (pow(y, k, n) * pow(u, r, n), pow(y, m, n) * pow(v, r, n))
    return (C, n, y, r)
    
print encrypt(flag)