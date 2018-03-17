# Assign string with decimal inserted to variable x
x = "There are %d types of people." % 10

# Assign two variables
binary = "binary"
do_not = "don't"

# Assign string with two string format characters to variable y
y = "Those who know %s and those who %s." % (binary, do_not)

# Print both strings
print x
print y

# Print two strings, with different string format characters, %r and %s
print "I said: %r." % x
print "I also said: '%s'." % y

# Assign two variables, one with a string format character
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Print combination of both previous variables, one of which is the string format character
print joke_evaluation % hilarious

# Assign two more variables
w = "This is the left side of..."
e = "a string with a right side."

# Concatenate both variables together and print them out
print w + e
