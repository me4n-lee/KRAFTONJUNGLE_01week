#https://www.acmicpc.net/problem/10871
#X보다 작은 수

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] < x:
        print(a[i], end=" ")
