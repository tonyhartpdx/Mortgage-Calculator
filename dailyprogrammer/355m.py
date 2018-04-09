#!/usr/bin/python

'''
[2018-03-28] Challenge #355 [Intermediate] Possible Number of Pies
https://www.reddit.com/r/dailyprogrammer/comments/87rz8c/20180328_challenge_355_intermediate_possible/
'''

import operator

recipes = {
    'apple': [1,4,3,2],
    'pumpkin': [1,3,4,3]
}

Amax, Pmax = 0, 0

#The numbers represent the number of synthetic pumpkin flavouring, apples, eggs, milk and sugar 
inputs = [
    [10,14,10,42,24],
    [12,4,40,30,40],
    [12,14,20,42,24]
]

def bake(type, amt):
# Determine the amount of ingredients used in baking the given amount of pies of each type
    global pies, recipes
    used = map(lambda x: x*amt, recipes[type])
    used = [used[0],0,used[1],used[2],used[3]] if type == 'pumpkin' else \
        [0,used[0],used[1],used[2],used[3]]

    return used
    

def maxpies(ing):
# Determine max pies of each type to be baked from given ingredients list
    global Amax, Pmax
    a = ing.pop(1)
    Pmax = min(map(operator.div, ing, recipes['pumpkin']))

    p = ing.pop(0)
    ing.insert(0,a)
    Amax = min(map(operator.div, ing, recipes['apple']))

for i in inputs:
    totalpies = []
    ing = i[:]
    maxpies(i)
    for x in range(Pmax, -1, -1):
        left = map(operator.sub, ing, bake('pumpkin', x))
        maxpies(left)
        if x + Amax > sum(totalpies):
            totalpies = [x, Amax]

    print "%d Pumpkin Pies and %d Apple pies" % tuple(totalpies)
