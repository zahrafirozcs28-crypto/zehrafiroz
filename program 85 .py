from collections import Counter

def frequency_sort(s):
    freq = Counter(s)
    
    sorted_chars = sorted(s, key=lambda x: (freq[x], x))
    
    return "".join(sorted_chars)

s1 = "geeksforgeeks"
print(frequency_sort(s1))

s2 = "abc"
print(frequency_sort(s2))
