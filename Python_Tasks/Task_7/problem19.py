
# Problem: Weighted Uniform Strings
# Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input().strip()
n = int(input())
weights = set()
count = 0
prev = ""
for c in s:
    count = count + 1 if c == prev else 1
    weights.add((ord(c) - 96) * count)
    prev = c
for _ in range(n):
    print("Yes" if int(input()) in weights else "No")
