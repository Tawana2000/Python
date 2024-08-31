#program to print the item present at a given index. If the index is out of bounds, print Wrong index.

try:

    cars = ['BMW','Ferari','Audi','Tesla']

    index = int(input())

    print(cars[index])

except:
    print('Wrong Index')