#https://www.acmicpc.net/problem/2562
#최댓값
#2562

import sys
input = sys.stdin.readline

a = [0] * 9
for i in range(9):
    a[i] = int(input())

# print(a)

print(max(a))

for i in range(9):
    if a[i] == max(a):
        result = i+1
        print(result)
