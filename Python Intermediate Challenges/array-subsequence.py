# Write a program to check if is the subsequence
def subsequence(arr, seq):
    j = 0
    for val in arr:
        if j == len(seq):
            break
        if seq[j] == val:
            j += 1
    return j == len(seq)

print(subsequence([12, 6, 8, 51, 9, 23,-18, 10], [1, 6, -18, 10]))
print(subsequence([12, 6, 8, 51, 9, 23,-18, 10], [12, 6, 8, 51, 9,23,-18, 10]))
print(subsequence([100,40,23],[100,40]))
print(subsequence([56,20,80,78],[20]))
