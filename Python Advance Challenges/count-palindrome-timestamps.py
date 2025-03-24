# Write a function to count the number of occurrence of palindrome timestamps within a given time range

def count_palindrome_timestamps(start_time, end_time):
    
    h1, m1 = map(int, start_time.split(":"))
    h2, m2 = map(int, end_time.split(":"))
    count = 0
    while (h1 < h2) or (h1 == h2 and m1 <= m2):
        if h1 // 10 == m1 % 10 and h1 % 10 == m1 // 10:
            count += 1
        m1 += 1
        if m1 == 60:
            m1 = 0
            h1 += 1
    return count

print(count_palindrome_timestamps("12:21", "15:51"))
