"""Collatz Conjecture - 
Start with a number n > 1. Find the number of steps it takes to reach one using
the following process: If n is even, divide it by 2. If n is odd, multiply it
by 3 and add 1."""

steps = 0
seq = []

start_number = raw_input("Enter a number greater than 1: ")
number = int(start_number)
seq.append(number)

while number > 1:
    if (number % 2 == 0):
        number /= 2
    else:
        number = (number * 3) + 1

    steps += 1
    seq.append(number)

print "%d steps to reduce %s to 1 using the Collatz Conjecture" % (steps, start_number)
print "Sequence: ", str(seq)[1:-1]
