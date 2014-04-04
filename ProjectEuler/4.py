total = 0
pals = []
def isPal(n):
    if str(n)[::-1] != str(n):
        return False
    else:
        return True

i,j = (100,100)
while True:
    while True:
        if isPal(i * j) == True and i * j > total:
            total = i * j
        j += 1
        if j == 1000:
            break
    i += 1
    j = 1
    if i == 1000:
        break

print total       

