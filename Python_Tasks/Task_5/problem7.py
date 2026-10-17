
# Problem Name: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == "__main__":
    m = int(input())
    set1 = set(map(int, input().split()))

    n = int(input())
    set2 = set(map(int, input().split()))

    result = sorted(set1.symmetric_difference(set2))

    for num in result:
        print(num)
