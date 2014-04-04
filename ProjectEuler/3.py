from math import sqrt
def isPrime(n):
    i=2
    while True:
        if n%i == 0:
            return False
        if i > n**(.5):
            return True
        i+=1

factors = []

number, largest, i = (600851475143, 0, 1)
root = sqrt(number)

while True:
    if number % i == 0:
        factors.append(i)
    i += 1
    if i > root:
        break

for i in factors:
    if isPrime(i) == True and i > largest:
        largest = i

print largest
