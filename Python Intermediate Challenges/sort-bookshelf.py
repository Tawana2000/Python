# Write a function to sort the bookshelf based on author's names

def sort_books(books):

    return sorted(books, key = lambda x: x['author'])

books = [
    {'title': 'Book3', 'author': 'Author3'},
    {'title': 'Book4', 'author': 'Author4'},
    {'title': 'Book5', 'author': 'Author2'}
]

print(sort_books(books))