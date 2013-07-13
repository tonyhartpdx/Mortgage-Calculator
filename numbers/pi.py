""""Find PI to the Nth Digit - 
Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go."""

import math

precision = int(raw_input("How many spaces? "))

while precision > 50:
	print "Number to large"
	precision = int(raw_input("How many spaces? "))
else:
	print '%.*f' % (precision, math.pi)
