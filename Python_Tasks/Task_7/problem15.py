
# Problem: Game of Thrones - I
# Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter
s = input().strip()
odd = sum(v % 2 for v in Counter(s).values())
print("YES" if odd <= 1 else "NO")
