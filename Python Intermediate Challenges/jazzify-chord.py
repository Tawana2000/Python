# Write a function to jazzify every chord in a list

def jazzify_chords(chords):

    result = []
    for i in chords:
        result.append(i + '7')
    return result    
    
print(jazzify_chords(['G', 'F', 'C']))