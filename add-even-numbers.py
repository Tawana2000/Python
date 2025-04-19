#Write a function to add even numbers from 1 to n

def add_even(n):

    even_no = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            even_no += i

    return even_no

n = 20
print(add_even(n))
