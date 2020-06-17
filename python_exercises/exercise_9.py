# Variables and Names

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are {} cars available.".format(cars))
print("There ara only {} drivers available.".fomat(drivers))
print("There will be {} empty cars today.".format(cars_not_driven))
print("We can transport {} people today."format(carpool_capacity))
print("We have {} to carpool today.".format(passengers))
print("We need to put about {} in each car.".format(average_passengers_per_car))
