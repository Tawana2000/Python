#Program to convert decimal to binary using recursion

def find_binary(decimal):

    if decimal == 0:
        return ""
    
    return find_binary(decimal // 2) + str(decimal % 2)

print(find_binary(12))