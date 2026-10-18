
# Problem: Sherlock and the Valid String
# Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter
from collections import Counter
freq = Counter(Counter(input().strip()).values())
if len(freq) == 1 or (len(freq) == 2 and (1 in freq.values()) and (freq[min(freq)] == 1 or max(freq) - min(freq) == 1)):
    print("YES")
else:
    print("NO")
