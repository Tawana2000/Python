# Write a function to group the anagrams together from a given list of strings

def group_anagrams(strs):

    anagrams = {}

    for s in strs:
        key = ''.join(sorted(s))

        if key in anagrams:
            anagrams[key].append(s)

        else:
            anagrams[key] = [s]

    sorted_anagrams = [sorted(group) for group in anagrams.values()]
    sorted_anagrams.sort

    return sorted_anagrams

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))