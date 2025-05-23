# Write a function to check if four given words can be completely segmented from the string. 

def can_segment_string(s, words = ['apple', 'pear', 'pier', 'pie']):

    return s == "" or any(s.startswith(w) and can_segment_string(s[len(w):]) for w in words)

print(can_segment_string("applepiearpier"))
print(can_segment_string("applepiepier"))  
print(can_segment_string("applepiep"))  
