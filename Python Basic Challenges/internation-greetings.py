# Write a function to return a greeting in different languages based on the country name provided.

def greet(country):

    greetings = {'USA': 'Hello',
                'France': 'Bonjour',
                'Spain': 'Hola', 
                'Germany': 'Hallo', 
                'Italy': 'Ciao'}
    
    return greetings.get(country, 'Greeting not in the list')

print(greet('France'))
print(greet('Italy'))