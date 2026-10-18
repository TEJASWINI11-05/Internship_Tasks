
# Problem: Anagram
# Link: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter
for _ in range(int(input())):
    s = input().strip()
    if len(s) % 2:
        print(-1)
    else:
        mid = len(s) // 2
        print(sum((Counter(s[:mid]) - Counter(s[mid:])).values()))
