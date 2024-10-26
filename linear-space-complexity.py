"""
Linear space complexity O(n)

An algorithm has a linear space complexity if the amount of memory required to execute is proportional to the size of the input.

input increase ---> memory required increases
input decreases ---> memory required decreases
"""

def find_sum(number):        # n   can be n numbers

    total = 0

    for i in number:           # 1
        total = total + i      # 1

    return total

print(find_sum([1,2,3,4]))