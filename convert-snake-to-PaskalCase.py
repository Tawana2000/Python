#Create a Python program that converts snake_case strings to PascalCase.
#In snake case, all words are in lowercase but separated by an underscore. For example, this_is_written_in_snake_case.
#In pascal case, each word is separated by the first uppercase letter. For example, ThisIsWrittenInPascalCase.

def pas_case(string):

    new_str = ''
    counter = 0   #to count the string characters

    while counter < len(string):

        if counter == 0:
                new_str += string[counter].upper()

        elif string[counter] == '_':
             new_str += string[counter + 1].upper()

             counter += 1
        
        else:
             new_str += string[counter]

        counter += 1

    return new_str

result = pas_case('custom_date_builder')
print(result)
