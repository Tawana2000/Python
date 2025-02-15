# Write a function to determine whether a given string represents stalactites or stalagmites

def identify_formation(s):

    lines = s.split("\n")
    mid = len(lines) // 2

    top_count = sum(line.count("#") for line in lines[:mid])
    bottom_count = sum(line.count("#") for line in lines[mid:])

    return "Stalactites" if top_count > bottom_count else "Stalagmites" if bottom_count > top_count else "Both"

# Test cases
print(identify_formation("###\n ###"))
print(identify_formation("###\n#"))
print(identify_formation("###\n#\n#\n###"))