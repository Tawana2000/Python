#Create a Python program to increment the values of a dictionary by 1.


def increment(dictionary):

    for key in dictionary:
        dictionary[key] += 1

    print(dictionary)

player_score = {
    'Cody' : 50,
    'Jack' : 57,
    'Seth' : 59,
    'Roman' : 67,
}

increment(player_score)