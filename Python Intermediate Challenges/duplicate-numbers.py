# Write a function to return all duplicate numbers from a given list

def find_duplicates(numbers):

    duplicates = []

    for i in numbers:
        if numbers.count(i) > 1:
            duplicates.append(i)

    return list(set(duplicates))

numbers = [1, 2, 3, 2, 1]
print(find_duplicates(numbers))