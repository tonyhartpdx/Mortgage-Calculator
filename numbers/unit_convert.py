"""Unit Converter (temp, currency, volume, mass and more) -
Converts various units between one another. The user enters 
the type of unit being entered, the type of unit they want to 
convert to and then the value. The program will then make the
conversion."""

import os

os.system('clear')

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

def volume():
	return true

def mass():
	return true

def currency():
	return true


print """1: Temperature
2: Volume
3: Mass
4; Currency"""

input = input("Enter conversion type: ")

if input == 1:
	temp()
elif input == 2:
	volume()
elif input == 3:
	mass()
elif input == 4:
	currency()
else:
	print "Invalid selection"
