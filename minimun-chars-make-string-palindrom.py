#Write a Python program to print the minimum number of characters required to make a string a palindrome.

string = 'joe'
counter = 0

while len(string) > 0:

    if string == string[::-1]:
        break

    else:
        counter += 1
        string = string[:-1]

print(counter)