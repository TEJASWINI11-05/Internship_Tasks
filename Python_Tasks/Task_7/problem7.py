
# Problem: Alphabet Rangoli
# Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    letters = string.ascii_lowercase
    for i in range(size - 1, -size, -1):
        row = "-".join(letters[abs(i):size])
        print((row[::-1] + row[1:]).center(4 * size - 3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
