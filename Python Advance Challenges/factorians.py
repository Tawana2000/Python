# Write a functio to find all the factorians within a range
# A factorian is a natural number that equals the sum of the facotrials of its decimal digits. For example, 145 is a factorian because 1! + 4! + 5! = 145

import math 
def find_factorians(start, end):

    result = []

    for i in range(start, end + 1):
        if sum(math.factorial(int(d)) for d in str(i)) == i:
            result.append(i)

    return result

print(find_factorians(1, 500))
