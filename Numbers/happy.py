"""Happy Numbers -  A happy number is defined by the following process. Starting
with any positive integer, replace the number by the sum of the squares of its
digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for
which this process ends in 1 are happy numbers, while those that do not end in 1
are unhappy numbers. Take an input number from user, and find first 8 happy
numbers from that input."""

start = input = number = int(raw_input("Enter a number greater than 1: "))
seq, found, count = [], [], 0

def reset(happy = 0):
    global count, number, seq, found, input
    seq = []
    input += 1
    number = input
    if happy > 0:
        count += 1
        found.append(happy)

while count < 8:
    total = 0
    for d in str(number):
        total += int(d)**2
        
    if total in seq:
        reset()
    elif total == 1:
        reset(input)
    else:
        seq.append(total)
        number = total

print "First 8 happy numbers starting at %d:" % start, found
