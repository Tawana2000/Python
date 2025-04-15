# Write a program to find the area of a right angeld tringle rounded off to two decimal places

def right_triangel_are(base, height):
    
    result = (1/2)*base * height
    return float(result)

base = int(input('Enter the base value: '))
height = int(input('Enter the height value: '))
print(right_triangel_are(base, height))
