# Write a function to find the index of a given element in a list

def find_index(lst, n):

    for i in range(len(lst)):
        if lst[i] == n:
            return i
        
    return 'Element not found'
    
lst = list(map(int, input('Enter the list elements separated by space: ').split()))
n =int(input('Enter the number to check the index: '))

print(find_index(lst, n))