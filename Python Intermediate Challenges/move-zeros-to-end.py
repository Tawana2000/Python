#Create a Python program to move all the zero (0) elements of a list to the end of the list.

l = [1, 0, 2, 0, 4, 0, 6, 5]

for i in l:
    if i == 0:

        l.remove(i)

        l.append(i)
print(l)