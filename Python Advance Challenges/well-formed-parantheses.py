# Write a function to generate all combinations of well-formed parentheses for a given number of pairs

def generate_parentheses(n):

    result = []
    def generate(s = "", open_n = 0, close_n = 0):
        if len(s) == 2 * n:
            result.append(s)

        else:
            if open_n < n:
                generate(s + "(", open_n + 1, close_n)

            if close_n < open_n:
                generate(s + ")", open_n, close_n + 1)

    generate()
    return result

print(generate_parentheses(3))