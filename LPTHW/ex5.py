name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
centimeters = height * 2.54
kilos = weight * .453592

print "Let's talk about %r." % name
print "He's %d inches tall, or %d centimeters." % (height, centimeters)
print "He's %d pounds heavy, or %d kilograms." % (weight, kilos)
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
