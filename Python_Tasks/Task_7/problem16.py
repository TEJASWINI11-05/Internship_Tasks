
# Problem: Caesar Cipher
# Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

n = int(input())
s = input().strip()
k = int(input()) % 26
result = ""
for c in s:
    if c.islower():
        result += chr((ord(c) - 97 + k) % 26 + 97)
    elif c.isupper():
        result += chr((ord(c) - 65 + k) % 26 + 65)
    else:
        result += c
print(result)
