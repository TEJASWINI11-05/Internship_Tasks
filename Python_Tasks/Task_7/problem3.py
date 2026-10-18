
# Problem: Mars Exploration
# Link: https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
print(sum(a != b for a, b in zip(s, "SOS" * (len(s) // 3))))

