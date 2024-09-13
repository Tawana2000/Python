#Problem Description, Suppose you are in a restaurant with your friends. You get a bill of a certain amount. If the tax rate is 8.875%, find out how much should each of you pay equally.

def bill(amount):

    no_guest = int(input('Number of guests: '))
    tax = (amount * 8.875) / 100

    total = (tax + amount ) / no_guest

    print(total)

amount = int(input('Enter the total amount: '))
bill(amount)