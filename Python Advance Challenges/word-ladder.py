# Write a function word_ladder(start, end, word_dict) that returns the length of the shortest transformation sequence or 0 if no such sequence exists.

from collections import deque

def word_ladder(start, end, word_dict):
    word_dict.add(end)
    queue = deque([(start, 1)])
    
    while queue:
        word, length = queue.popleft()
        if word == end:
            return length
        
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_dict:
                    word_dict.remove(new_word)
                    queue.append((new_word, length + 1))
    return 0

word_dict = set(["hot", "dot", "dog", "lot", "log", "cog"])
print(word_ladder("hit", "cog", word_dict)) 
