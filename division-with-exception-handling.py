#program to divide numerator by denominator. However, if the denominator is 0, print Denominator cannot be 0. Try again.

try:


    numerator = int(input())
    denominator = int(input())

    result = numerator / denominator

    print(result)

except:
    if denominator == 0:
        print('Denominator cannot be 0. Try again.')