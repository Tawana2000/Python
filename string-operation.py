# Write a function to check if the user likes a car or a bike

def check_preference(preference):

    preference = preference.lower()

    if 'car' in preference:
        return 'You like car.'
    
    elif 'bike' in preference:
        return 'You like bike.'
    
preference = 'cAr'
print(check_preference(preference))