# Write a function to concatenate individual items of a list

def concatenate_items(items):

    result = " "
    for i in items:
        result += i

    return "'" + result.strip() + "'"
items = ['Hello', 'World']
print(concatenate_items(items))