i=0
j=1
a=0
while True:
    x=i+j
    if x > 4000000:
        break
    if x%2==0:
        a+=x
    i=j
    j=x
print a
