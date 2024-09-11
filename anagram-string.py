#Create a Python program to check if two strings are anagrams.
# two strings are anagram if we can form one string by re arranging the other string like: 'race', 'care'

def anagram(str1,str2):

    str1.replace(' ','')
    str2.replace(' ','')

    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1 == str2:
        print('Anagram')
    else:
        print('Not Anagram')
    
str1 = 'race'
str2 = 'care'
anagram(str1,str2)