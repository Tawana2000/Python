# Write a function to check if a given number is a Kaprekar number or not
# A Kaprekar number is a number whose square can be split ito two parts that add up to the original number again

def is_kaprekar(n):
    if n <= 0:
        return False
    
    square = n * n
    s = str(square)
    length = len(s)
    
    if length == 1:
        return square == n
    
    mid = length // 2
    left = int(s[:mid]) if s[:mid] else 0
    right = int(s[mid:]) if s[mid:] else 0
    
    return left + right == n

print(is_kaprekar(45))  
print(is_kaprekar(9))  
print(is_kaprekar(10))
