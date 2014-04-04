total = 0
i=1
while True:
    if i % 3 == 0 or i % 5 == 0:
        total += i
    i += 1
    if i >= 1000:
        break
print total
