#create a Python program that calculates the total fuel needed and the extra fuel supplied to the car when the distance is given.
#A car needs 10 times more fuel than the distance it covers. But the car always has a minimum of 100 ltr of fuel in stock. This means that if the car needs to travel 15 km, it would need 150 ltr of fuel.
#But if a car needs to travel just 5 km, the car would need just 50 ltr of fuel. In this case, the car doesn't need extra fuel since it always has 100 ltr of fuel in stock. 

def fuel(km):

    required_fuel = km * 10

    if required_fuel < 100:

        extra_fuel = 0

    else:

        extra_fuel = required_fuel - 100


    return required_fuel, extra_fuel

km = int(input())
print(fuel(km))
