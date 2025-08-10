#Write a function that takes a string and returns all possible ways to partition it into palindromic substrings.

def partition_palindromes(s: str) -> list[list[str]]:
    def is_palindrome(start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def backtrack(start: int, path: list[str], result: list[list[str]]):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start, len(s)):
            if is_palindrome(start, end):
                path.append(s[start:end + 1])
                backtrack(end + 1, path, result)
                path.pop()
    
    result = []
    backtrack(0, [], result)
    return result
