# Write a function to create a numeric seesaw

def numeric_seesaw(n):
    
    if n <= 0:
        raise ValueError("Please enter a positive number!")
    
    lst1 = list(range(1, n + 1))
    lst2 = list(range(n - 1, 0 , -1))  # Reverse sequence excluding n
    return lst1 + lst2

n = int(input("Enter a number to create the seesaw: "))
print(numeric_seesaw(n))