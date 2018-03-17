def isPrime(n):
    i=2
    while True:
        if n%i == 0 and n > 2:
            return False
        if i > n**(.5):
            return True
        i+=1

p,x = (0,2)
while True:
  if isPrime(x) == True:
    p += 1
  if p == 10001:
  	break
  x += 1

print x
