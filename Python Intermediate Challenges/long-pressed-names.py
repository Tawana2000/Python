# Write a function to check if a string can be obtained by long pressing the keys of another string

def is_long_pressed(name, type):

    i = 0
    for j in range(len(type)):
        if i < len(name) and name[i] == type[j]:
            i += 1

        elif j == 0 or type[j] != type[j - 1]:
            return False
        
    return i == len(name)

print(is_long_pressed("saeed", "ssaaedd"))
print(is_long_pressed("alex", "aaleex"))
