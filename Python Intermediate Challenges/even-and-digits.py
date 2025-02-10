# Write a function to count the number of even and odd digits in a given 

def count_even_odd_digits(n):
    even_count = 0
    odd_count = 0

    for digit in str(abs(n)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)


number = 123456
print(count_even_odd_digits(number))