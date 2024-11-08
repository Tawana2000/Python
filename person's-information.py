# Write a function to return a person's information

def get_user_info(name, age, address):

    result = {"Name" : name, "Age" : age, "Address" : address}
    return result

name, age, address = [x.strip() for x in input('Enter your name, age, and address separated by comma: ').split(",")]

user_info = get_user_info(name, age, address)
print(f"Name: {user_info['Name']}\nAge: {user_info['Age']}\nAddress: {user_info['Address']}")