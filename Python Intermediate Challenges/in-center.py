# Write a function to check if a given string is in the center of another string

def is_in_center(s1, s2):

    if len(s1) > len(s2):
        return False
    
    start = (len(s2) - len(s1)) // 2

    if len(s2) % 2 == 0 and (len(s2) - len(s1)) % 2 != 0:
        return False
    
    return s2[start:start + len(s1)] == s1

print(is_in_center('hello', 'xxhelloxx')) 
print(is_in_center('test', 'mytestmy')) 
print(is_in_center('hi', 'world'))