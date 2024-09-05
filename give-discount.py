#Create a Python function that gives discounted prices.

def discount(disc,original):

    discounted = (original * disc) // 100
    result = original - discounted

    print(result)

discount(20,50)