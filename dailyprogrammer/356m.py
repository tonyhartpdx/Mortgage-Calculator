#!/usr/bin/python

'''
[2018-04-11] Challenge #356 [Intermediate] Goldbach's Weak Conjecture
https://www.reddit.com/r/dailyprogrammer/comments/8bh8dh/20180411_challenge_356_intermediate_goldbachs/
'''

import sys, random

primes = []
solutions = []
input = int(sys.argv[1])

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

for i in range(2,input):
    if is_prime(i):
        primes.append(i)

for a in primes:
    for b in primes:
        for c in primes:
            if a+b+c == input:
                solutions.append("%s + %s + %s" % (a,b,c))

print "%s = %s" % (input, random.choice(solutions))
