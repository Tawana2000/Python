#Given a list of numbers, find if the list elements are in ascending sequence or not a sequence at all., return True or False

def is_sequence(number):

    flag = True

    for i in range(len(number) - 1):

        if number[i] < number[i + 1]:
            continue

        else:
            flag = False
            break

    return flag


number = input().split()
print(is_sequence(number))