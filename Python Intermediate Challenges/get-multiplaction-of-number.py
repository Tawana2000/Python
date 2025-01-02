# Write a function to get the multiplication table of a number from 1 to 5

def multi_table(number):

    result = []

    for i in range(1, 6):
        product = i * number
        result.append(product)
        i += 1


    return result


number = int(input("Enter the number: "))
print(multi_table(number))