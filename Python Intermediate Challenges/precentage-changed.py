# Write a function to calculate the percentage change between two numbers 

def percentage_changes(old_number, new_number):

    return round(((new_number - old_number) / old_number) * 100, 2)

print(percentage_changes(100, 150))