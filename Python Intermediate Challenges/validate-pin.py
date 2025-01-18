# Write a function to validate a given PIN
# The PIN should be exactly 4 or 6 digits long and contains only numbers

def validate_pin(pin):
    
    if len(str(pin)) != 4 and len(str(pin)) != 6:
        return False
    
    return True
    
pin = int(input("Please enter a 4 or 6 digits PIN to validate: "))
print(validate_pin(pin))