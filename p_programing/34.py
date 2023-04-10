#https://www.acmicpc.net/problem/10989
#수 정렬하기 3
#10989

import sys
input = sys.stdin.readline

n = int(input())
n_list = [0] * 10001

for _ in range(n):
    a = int(input())
    n_list[a] += 1

for i in range(10001):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)
            #print(n_list[i])를 넣으니 내림차순이 됐다! 