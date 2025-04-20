"""
Constant space complexity or O(1)

An algorithm has constant space complexity if the amount of memory required for its execution doesn't change with the change in the input size
"""

def find_sum(n1,n2,n3):    # 1 + 1 + 1 SC for the input

    result = n1 + n2 + n3  # 1
    print(result)

find_sum(1,2,3)            # SC  = 4 = 1  = O(1)
