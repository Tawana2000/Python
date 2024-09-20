#Write a Python program to find the smallest missing integer in a list.

def smallest(lst):

    lst.sort()


    for index, number in enumerate(lst):

        if number + 1 == lst[index + 1]:
            continue


        else:
            return number + 1
        
numbers = [2, 4, 6, -1, 5, 1, 0]
print(smallest(numbers))