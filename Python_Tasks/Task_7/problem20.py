
# Problem: Super Reduced String
# Link: https://www.hackerrank.com/challenges/reduced-string/problem

s = input().strip()
stack = []
for c in s:
    if stack and stack[-1] == c:
        stack.pop()
    else:
        stack.append(c)
print("".join(stack) if stack else "Empty String")
