#Given a list of numbers that are already in ascending order, square the numbers. But the result should be in ascending order as well.

def sqaure(itmes):

    new_list = []


    for i in items:
        i = i * i
        new_list.append(i)
        new_list.sort()
    return new_list

items = input().split()
items = [int(i) for i in items]

print(sqaure(items))