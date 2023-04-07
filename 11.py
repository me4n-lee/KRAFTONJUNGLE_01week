#https://www.acmicpc.net/problem/10950
#A+B - 3

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a,b = map(int, input().split())
    print(a+b)
    
# for _ in range(n):
#     print(a+b)