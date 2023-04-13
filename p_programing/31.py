#https://www.acmicpc.net/problem/1074
#Z
#1074

import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def z(n, r, c):
    if n == 0:
        return 0
    half = (2 ** n) /2 
    if r < half and c < half:
        return z(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + z(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + z(n - 1, r - half, c)
    else:
        return 3 * half * half + z(n - 1, r - half, c - half)

print(z(n,r,c))

# n, r, c = map(int, input().split())

# if r%2 == 1 and c%2 == 1:
#     visit = 1
# elif r%2 == 0 and c%2 == 1:
#     visit = 2
# elif r%2 == 1 and c%2 == 0:
#     visit = 3
# elif r%2 == 0 and c%2 == 0:
#     visit = 4

# 1. r = 1, c = 1
# 2. r = 2, c = 1
# 3. r = 1, c = 2
# 4. r = 2. c = 2