"""**Change Return Program** -
he user enters a cost and then the amount of money given.
The program will figure out the change and the number of
quarters, dimes, nickels, pennies needed for the change."""

cost = float(raw_input("Enter cost of item: "))
given = float(raw_input("Enter amount given: "))

while given < cost:
	print "You still owe $%.2f" % (cost - given)
	given = float(raw_input("Enter amount given: "))

tw,te,f,o,q,d,n,p = 0,0,0,0,0,0,0,0
dollars = int(given - cost)
change = (given - dollars - cost) * 100 #because floating point math sucks

if dollars >= 20:
	tw = int(dollars / 20)
	dollars = dollars % 20

if dollars >= 10:
	te = int(dollars / 10)
	dollars = dollars % 10

if dollars >= 5:
	f = int(dollars / 5)
	dollars = dollars % 5

if dollars >= 1:
	o = dollars

if change >= 25:
	q = int(change / 25)
	change = change % 25

if change >= 10:
	d = int(change / 10)
	change = change % 10

if change >= 5:
	n = int(change / 5)
	change = change % 5

if change >= 1:
	p = change

print "Your change is $%.2f: \n \
%.0f twenties \n \
%.0f tens \n \
%.0f fives \n \
%.0f ones \n \
%.0f quarters \n \
%.0f dimes \n \
%.0f nickels \n \
%.0f pennies" % (given - cost, tw, te, f, o, q, d, n, p)
