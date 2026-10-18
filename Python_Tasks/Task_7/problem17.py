
# Problem: Separate the Numbers
# Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

for _ in range(int(input())):
    s = input().strip()
    found = False
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        value = first
        built = ""
        while len(built) < len(s):
            built += str(value)
            value += 1
        if built == s:
            print("YES", first)
            found = True
            break
    if not found:
        print("NO")
