#Create a Python program to break a list into chunks of 4 elements.

numbers = [2, 3, 6, 7, 3, 5, 7, 8, 9, 2, 20, 24, 16, 17, 23, 19]
chunks = [] #to store the chucnked elements

for i in range(0,len(numbers), 4): #take for to slice away four elements each time

    chunk = numbers[i : i + 4]

    chunks.append(chunk)

for chunk in chunks:
    print(chunk)
