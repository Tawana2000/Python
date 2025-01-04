# Write a function to find a subsequence of a given list of integers

"""
- Define a function that takes a list of integers and an integer k as input
- Inside the function, calculate the sum for each subsequence of lenght k
- Return the maximum sum found
"""

def largest_sum_subsequence(numbers, k):

    if k > len(numbers) or k <= 0:
        return "K must be between 1 and the lenght of the given list!"
    
    return max(sum(numbers[i:i + k]) for i in range(len(numbers) - k + 1))

numbers = list(map(int, input("Enter the list elements separated by space: ").split()))
k = int(input("Enter the K value: "))
print(largest_sum_subsequence(numbers, k))