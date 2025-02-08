# Write a function to determine if a rhythm is syncopated

def is_syncopated(rhythm):

    return 'Yes' if " " in rhythm  else 'No'

print(is_syncopated("+++"))
print(is_syncopated("++ ++++ +"))