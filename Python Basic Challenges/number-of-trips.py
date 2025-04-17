# Write a function to calculate the number of trips a driver has to make to transport 12 passengers
# The driver can only carry a limited number of passengers at a time (provided as input), and you need to return how many trips are required.

def number_of_trips(seats):

    return 12 // seats

print(number_of_trips(3))