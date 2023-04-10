#https://www.acmicpc.net/problem/10971
#외판원 순회 2
#10971

import sys
input = sys.stdin.readline

n = int(input())
road_list = []
for i in range(n):
    road = list(map(int, input().split()))
    road_list.append(road)

print(road_list)