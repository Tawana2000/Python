# Write a program to split the resturant bill among friends considering 20% tax

def bill(amount, no_friends):
    return float(amount + tax) / no_friends

amount = int(input('Enter the total amount: '))
no_friends = int(input('Enter the number of people who wants to pay: '))
tax = (amount * 20) / 100
print(bill(amount, no_friends))
