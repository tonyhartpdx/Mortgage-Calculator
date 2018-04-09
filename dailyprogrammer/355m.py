#!/usr/bin/python

'''
[2018-03-28] Challenge #355 [Intermediate] Possible Number of Pies
https://www.reddit.com/r/dailyprogrammer/comments/87rz8c/20180328_challenge_355_intermediate_possible/
'''

import operator

recipes = {
    'apple': [0,1,4,3,2],
    'pumpkin': [1,0,3,4,3]
}

ingredients = [
    [10,14,10,42,24],
    [12,4,40,30,40],
    [12,14,20,42,24]
]

Amax, Pmax = 0, 0

def maxpies(type, ing):
    pies = [int(i/r) if i and r else 0 for i, r in zip(ing,recipes[type])]
    return min([p for p, r in zip(pies, recipes[type]) if r])

for i in ingredients:
    totalpies, ing = [], i[:]
    Pmax, Amax = maxpies('pumpkin',i), maxpies('apple',i)
    for x in range(Pmax, -1, -1):
        Amax = maxpies('apple',map(operator.sub, ing, 
            map(lambda y: x*y, recipes['pumpkin'])))
        totalpies = [x, Amax] if x + Amax > sum(totalpies) else totalpies

    print "%d Pumpkin Pies and %d Apple pies" % tuple(totalpies)
