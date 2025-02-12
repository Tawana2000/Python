# Write a function to retrieve the name from a email address

def get_name_from_email(email):

    name_part = email.split('@')[0]
    name = name_part.replace('.', " ")
    return name

email = 'john.doe@example.com'
print(get_name_from_email(email))