# Write a function to filter all multiples of three

def filter_multiples_three(n):
    
    result = []

    for i in range(1, n + 1):
        if i % 3 != 0:
            result.append(i)

    return result

n = int(input("Enter a number: "))
print(filter_multiples_three(n))