#Write a function to convert Celsius to Fharnheight 
def celsius_to_fahrenheit(celsius):
    return [(temp * 9/5) + 32 for temp in celsius]

print(celsius_to_fahrenheit([0, 20, 37]))  # [32.0, 68.0, 98.6]
