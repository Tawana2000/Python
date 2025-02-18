# Write a function to generate the Baumsweet sequence up to a given number

def baumsweet_sequence(n):
    result = []
    for i in range(1, n + 1):
        binary = bin(i)[2:]
       
        zero_blocks = binary.split('1')
        
        if all(len(block) % 2 == 0 for block in zero_blocks):
            result.append(1)
        else:
            result.append(0)
    return result

print(baumsweet_sequence(3))  
print(baumsweet_sequence(5))