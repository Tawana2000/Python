#Write a Python program that takes two integer parameters and checks if the sum of digits in each parameter is equal, ex: 900 --> 9+0+0 = 9 and 243 --> 2 + 4 + 3 = 9

def equal_sum(n1, n2):

    first_sum = 0       #sum of first number 
    second_sum = 0      #sum of second number

    for i in str(n1):
        first_sum += int(i)

    for j in str(n2):
        second_sum += int(j)

    if first_sum == second_sum:
        return True
    
    else:
        return False
    
n1 = input()
n2 = input()

print(equal_sum(n1, n2))