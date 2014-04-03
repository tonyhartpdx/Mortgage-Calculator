"""Unit Converter (temp, currency, volume, mass and more) -
Converts various units between one another. The user enters 
the type of unit being entered, the type of unit they want to 
convert to and then the value. The program will then make the
conversion."""

import os, json
from urllib2 import urlopen

os.system('clear')

CONVERT_TO = {
    'volume': {
            'tsp': 48,
            'tbsp': 16,
            'c': 1,
            'q': .25,
            'p': .5,
            'gal': .0625,
            'oz': 8
        },
    'mass': {
            'g': 453.59,
            'oz': 16,
            'lb': 1,
            'kg': 0.45359
        }
}

CONVERT_FROM = {
    'volume': {
            'tsp': .015625,
            'tbsp': .0625,
            'c': 1,
            'q': 4, 
            'p': 2, 
            'gal': 16,
            'oz': .125
        },
    'mass': {
            'g': .0022046,
            'oz': .0625,
            'lb': 1,
            'kg': 2.2406
        }
}

def temp():
	print """\n1: Celsius to Fahrenheit
2. Celsius to Kelvin
3. Fahrenheit to Celsius
4. Fahrenheit to Kelvin
5. Kelvin to Celsius
6. Kelvin to Fahrenheit"""

	choice = int(raw_input("Enter conversion type: "))

	if choice == 1:
		degrees = int(raw_input("Enter temperature to convert: "))
		result = (degrees * 1.8) + 32
		unit = 'F'
	elif choice == 2:
		degrees = int(raw_input("Enter temperature to convert: "))
		result = degrees + 273.15
		unit = 'K'
	elif choice == 3:
		degrees = int(raw_input("Enter temperature to convert: "))
		result = (degrees - 32) / 1.8
		unit = 'C'
	elif choice == 4:
		degrees = int(raw_input("Enter temperature to convert: "))
		result = ((degrees - 32) / 1.8) + 273.15
		unit = 'K'
	elif choice == 5:
		degrees = int(raw_input("Enter temperature to convert: "))
		result = degrees - 273.15
		unit = 'C'
	elif choice == 6:
		degrees = int(raw_input("Enter temperature to convert: "))
		result = ((degrees - 273.15) * 1.8) + 32
		unit = 'F'
	else:
		print "Invalid selection"
		temp()

	print "Value: " + str(result) + ' ' + unit

def do_convert(conversion):
    conversion_units = ','.join(CONVERT_FROM[conversion].keys())
    amount = float(raw_input("Enter conversion amount:"))
    source_unit = raw_input("Enter source unit (%s):" % conversion_units)
    to_unit = raw_input("Enter unit to convert to (%s):" % conversion_units)
    
    print "%s %s's equals %f %s's" % (amount, source_unit, 
            amount * \
            CONVERT_FROM[conversion][source_unit] * \
            CONVERT_TO[conversion][to_unit],
            to_unit)

def currency():
    amount = str(raw_input("Enter amount to convert: "))
    from_currency = str(raw_input("Enter your source currency (3 digit code): "))
    to_currency = str(raw_input("Enter the currence you would like to convert to (3 digit code): "))

    request = urlopen('http://rate-exchange.appspot.com/currency?from=' + from_currency + '&to=' + to_currency + '&q=' + amount)
    response = json.loads(request.read())

    print "%s %s is equal to %f %s" % (amount, from_currency, float(response['v']), to_currency)


print """1: Temperature
2: Volume
3: Mass
4: Currency"""

input = input("Enter conversion type: ")

if input == 1:
    temp()
elif input == 2:
    do_convert('volume')
elif input == 3:
    do_convert('mass')
elif input == 4:
    currency()
else:
	print "Invalid selection"
