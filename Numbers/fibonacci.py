"""Fibonacci Sequence -
Enter a number and have the program generate the Fibonacci 
sequence to that number or to the Nth number."""

limit = int(raw_input("How far to go? "))
fibo = [0]

while len(fibo) < min(20, limit):
	if limit == 1:
		break
	elif len(fibo) == 1:
		fibo.append(1)
	else:
		fibo.append(fibo[-1] + fibo[-2])

print fibo
