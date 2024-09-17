#Write a Python program that checks whether the given number is Lapindrome or not.
#A Lapindrome Number is a number, which when split in the middle, gives two halves having the same characters and the same frequency of each character, for ex: 1234321

def lapindrome(number):

    middle_index = len(number) // 2

    first_half = number[:middle_index]

    if len(number) % 2 == 0:

        second_half = number[middle_index:]

    else:

        second_half = number[middle_index + 1:]

    first_half = ''.join(sorted(first_half))
    second_half = ''.join(sorted(second_half))

    
    if first_half == second_half:
        return 'It is Lapindrome Number'
    
    else:
        return 'It is not Lapindrome Number'
    

number = input()
print(lapindrome(number))