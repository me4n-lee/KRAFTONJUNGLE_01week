#https://www.acmicpc.net/problem/2751
#수 정렬하기2
#2751

import sys
input = sys.stdin.readline

n = int(input())
n_list = [] * n
for i in range(n):
    a = int(input())
    n_list.append(a)

# print(n_list)

n_list.sort()

for i in range(n):
    print(n_list[i])