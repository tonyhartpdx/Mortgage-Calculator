"""Binary to Decimal and Back Converter -
Develop a converter to convert a decimal number to 
binary or a binary number to its decimal equivalent."""

def b_to_d(number):
	rev = str(number)[::-1]
	counter = 0
	decimal = 0
	while counter < len(rev):
		if int(rev[counter]) == 1:
			decimal += 2**counter
		counter += 1
	return decimal

def d_to_b(number):
	binary = ''
	while number > 0:
		binary += str(number % 2)
		number = number / 2
	return binary[::-1]

print """
	1. Binary to Decimal Conversion
	2. Decimal to Binary Conversion\n"""

choice = input("Choose conversion type: ")

if choice == 1:
	number = input("Number to convert: ")
	print "Decimal of %s is %s" % (number, b_to_d(number))
elif choice == 2:
	number = input("Number to convert: ")
	print "Binary of %s is %s" % (number, d_to_b(number))
else:
	print "Invalid Choice"
