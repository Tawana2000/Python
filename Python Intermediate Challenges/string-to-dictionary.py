# Write a function to convert a string into a dictionary 

def string_to_dict(s):
    
    return {item.split(':')[0]: item.split(':')[1] for item in s.split(', ')}

print(string_to_dict('fruit:apple, color:red, taste:sweet'))