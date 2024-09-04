#Create a Python program to create a new list from an existing list of strings by copying only those elements that start with a consonant.

fruits = ['apple', 'banana', 'pineapple', 'mango', 'watermelon']

new_fruit = [fruit for fruit in fruits if fruit[0] not in 'AEIOUaeiou']
print(new_fruit)