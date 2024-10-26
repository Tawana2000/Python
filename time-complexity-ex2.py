# Time comlexity for the following code

def print_numbers(n):

    i = 1
    k = 1

    while k < n:
        print(k)

        k = k + i

        i = i + 1

n = 10
print_numbers(n)


"""
for the 
       i (input)       k (ouput)
       1               1
       2               1 + 1
       3               2 + 2
       4               2 + 2 + 3
       5               2 + 2 + 3 + 4

       m               2 + 2 + 3 + 4 + .... + m-1

the program ends when k >= n because of the condition of the while loop, let's assume this condition is reached when i reached a certain value, let's say m. 

then from the above table, we can say

k = 2 + 2 + 3 + 4 + .... + m-1 [approximatgely equal to sum of natural numbers]

k = m(m+1) / 2 [formula for sum of natural numbers]

m(m+1) / 2 >= n

m**2 = n   because [m(m+1) / 2] is equal to m square

m = n**(1/2) or m = root square of n

so

Time complexity = O(n**(1/2)) = O(root square of n)

"""