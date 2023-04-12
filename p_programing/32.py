#https://www.acmicpc.net/problem/2750
#수 정렬하기
#2750

import sys
input = sys.stdin.readline

n = int(input())
n_list = [] * n
for _ in range(n):
    a = int(input())
    n_list.append(a)

# n_list = list(map(int, input()))
# n_list = [map(int, input()) for i in range(n)]
# print(n_list)

n_list.sort()
# n_list = sorted(n_list,e)

for i in range(n):
    print(n_list[i])