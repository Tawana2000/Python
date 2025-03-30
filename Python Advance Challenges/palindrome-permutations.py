# Write a function all_palindrome_permutations(s) that returns a list of all valid palindrome permutations of the input string s.

from collections import Counter

def can_form_palindrome(s: str) -> bool:
    counts = Counter(s)
    odd_count = sum(1 for count in counts.values() if count % 2 != 0)
    return odd_count <= 1

def generate_palindrome(s: str, left: int, right: int, result: set):
    if left >= right:
        result.add(''.join(s))
        return
    s[left], s[right] = s[right], s[left]
    generate_palindrome(s, left + 1, right - 1, result)

def all_palindrome_permutations(s: str):
    if not can_form_palindrome(s):
        return []
    result = set()
    s = list(s)
    generate_palindrome(s, 0, len(s) - 1, result)
    return list(result)

print(all_palindrome_permutations("aab"))
