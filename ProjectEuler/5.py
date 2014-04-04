def isDiv(n):
    for i in range(11,21):
        if n % i != 0:
            return False
    return True

i=2520
while True:
    if isDiv(i) == True:
        break
    i += 2520

print i
