# Let's calculate the time complexity for the following code:

def print_numbers(n):

    i = 0
    j = 1

    while i < n:                  # n
        while j < n:              # n * logn
            print(j)              # n * logn

            j = j * 2             # n * logn

        i = i + 1                 # n

print_numbers(20)                 # result = 3nlogn + 2n

# the inner loop runs log(n) times in each iteration of the outer loop because the value of j is doubled every step. Hence, the inner loop operation runs n * log(n) times

# Time complexity = 3nlogn + 2n  = nlogn [highest term]  = O(nlogn)