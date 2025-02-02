# Write a function to get the top note of each student

def get_top_notes(student_notes):

    return {name: max(notes, default = 0) for name, notes in student_notes.items()}

student_notes = {
    'John': [3, 4, 5],
    'Jane': [6, 7, 8]
}

print(get_top_notes(student_notes))