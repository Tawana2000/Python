# Write a function to find the smallest sublist with a sum greater than a given value

def smallest_sublist(lst, target_sum):
    n = len(lst)
    min_length = float('inf')
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += lst[end]

        while current_sum >= target_sum: 
            min_length = min(min_length, end - start + 1)
            current_sum -= lst[start]
            start += 1

    return min_length if min_length != float('inf') else 0 


print(smallest_sublist([1, 2, 3, 4, 5], 9)) 