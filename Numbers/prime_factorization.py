"""Prime Factorization -
Have the user enter a number and find all 
Prime Factors (if there are any) and display them."""

def is_prime(n):
	if n % 2 == 0:
		return False

	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

input = int(raw_input("Enter a number: "))
factors = [1]
if input % 2 == 0:
	factors.append(2)

for x in range(3, int(input / 2) + 1):
	if input % x == 0:
		if is_prime(x) == True:
	 			factors.append(x)

print factors	
