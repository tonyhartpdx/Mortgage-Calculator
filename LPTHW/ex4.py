# 100 cars
cars = 100

# room for 4 people in a car
space_in_a_car = 4

# 30 drivers
drivers = 30

# 90 passengers
passengers = 90

# number of cars not driven equals total number of cars minus number of drivers
cars_not_driven = cars - drivers

# total number of cars driven equals total number of drivers
cars_driven = drivers

# carpool capacity equals cars driven times the amount of space in each car
carpool_capacity = cars_driven * space_in_a_car

# average number of passengers in each car equals total number passengers divided by the number of cars being driver
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
