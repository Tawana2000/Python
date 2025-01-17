# Write a function to generate and return the first n Cullen numbers
# A Cullen number is of the form n*2^n + 1 where n = 1, 2, 3.....

def cullen_number(n):
    
    cullen = 0
    result = [1]

    for i in range(1, n):
        cullen = i * (2 ** i) + 1
        result.append(cullen)
    #result.insert(0, 1)

    return result

n = 5
print(cullen_number(n))