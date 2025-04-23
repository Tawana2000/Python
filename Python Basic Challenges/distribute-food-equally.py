# Write a function to distribute food equally among people.

def distribute_food(food_items, people):

    return len(food_items) // people

print(distribute_food(['apple', 'banana', 'orange', 'grape'], 2))