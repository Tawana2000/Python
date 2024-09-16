#Given a list of numbers, find the sums of even numbers and odd numbers.

def sum_odd_even(lst):

    even_lst = []
    odd_lst = []

    for i in lst:

        if i % 2 == 0:
            even_lst.append(i)

        else:
            odd_lst.append(i)

    return sum(even_lst), sum(odd_lst)

lst = input().split()
int_lst = [int(x) for x in lst]
print(sum_odd_even(int_lst))