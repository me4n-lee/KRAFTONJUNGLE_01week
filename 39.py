#https://www.acmicpc.net/problem/2468
#안전 영역
#2468

import sys
input = sys.stdin.readline

n = int(input())
area_list = []
for i in range(n):
    area = list(map(int, input().split()))
    area_list.append(area)

print(area_list)

print(area_list[1][1])