# Write a function to generate a full name and email address.

def generate_email(first_name, last_name, domain):

    return {'Full Name': first_name + ' ' + last_name, 'Email': first_name[0].lower() + last_name.lower() + '@' + domain}

first_name = "John"
last_name = "Doe"
domain = "gmail.com"

print(generate_email(first_name, last_name, domain))