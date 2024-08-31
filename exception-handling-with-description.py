#program to print the value present at the given key. If the key is out of bounds, print Key is not available.

try:

    countries = {'Nepal':'Kathmandu','Sweden':'Stockholm','Italy':'Rome'}

    key = (input())

    print(countries[key])

except:
    print('Key is not available')