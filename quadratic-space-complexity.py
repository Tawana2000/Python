"""
Quadratic Space Complexity O(n**2)

An algorithm has quadratic space complexity if the amount of memory it takes to execute is proportional to the square of the input size.

input size increase ---> the memory required to execute the program increases quadratically
"""

def print_list_items(nested_list):

    for single_list in nested_list:      # n
        for item in single_list:        # n
            print(item)                 # Space complexity = O(n**2), multiplied cause of the nested loop


print_list_items([[1,2],[4,5]])