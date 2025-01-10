# Write a function to check if a number is a straight digital number
# A straight digital number is one where the difference between two consecutive digits is constant

def is_straight(n):

    digits = list(map(int, str(abs(n))))

    if len(digits) < 2:  #Single digit numbers are always straight
        return True
    diff = digits[1] - digits[0]
    return all(digits[i] - digits[i - 1] == diff for i in range(1, len(digits)))

print(is_straight(1234))
print(is_straight(3682))
print(is_straight(65432))