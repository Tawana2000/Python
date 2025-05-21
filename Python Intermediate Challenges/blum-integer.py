# Write a function to check if a given number is a Blum integer or not

def is_blum_integer(n):

    f, i = [], 2

    while i * i <= n:
        if n % i == 0:
            f.append(i)
            n //= i

        else:
            i += 1

    if n > 1:
        f.append(n)

    return len(f) == 2 and all(p % 4 == 3 for p in f)

print(is_blum_integer(21))
