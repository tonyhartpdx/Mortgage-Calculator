"""Coin Flip Simulation - 
Write some code that simulates flipping a single coin however many times the
user decides. The code should record the outcomes and count the number of tails
and heads."""
from random import *

outcomes = []

flips = int(raw_input("Number of coin flips to simulate? "))

while flips > 0:
    result = randint(1,2)
    outcomes.append(result)
    flips -= 1

print "Heads: %d" % outcomes.count(1)
print "Tails: %d" % outcomes.count(2)
