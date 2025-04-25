# Write a function to create a simple flashcard

def flash_card(question, answer):

    return {'Question' : question, 'Answer' : answer}

question = input('')
answer = input('')
print(flash_card(question, answer))