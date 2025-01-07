# Write a function to find the fulcrum of a list
# The fulcrum of a list is an integer such that all elements to the left and all elements to the right sum to the same level

def find_fulcrum(lst):

    total_sum = sum(lst)
    left_sum = 0

    for i, num in enumerate(lst):
        total_sum -= num

        if left_sum == total_sum:
            return i
        
        left_sum += num

    return None      #Return None if no fulcrum is found

lst = list(map(int, input("Enter the list elements separated by space: ").split()))
print(find_fulcrum(lst))