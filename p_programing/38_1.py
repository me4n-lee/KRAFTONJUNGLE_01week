# 백준 10971번: 외판원 순회 2
# https://www.acmicpc.net/problem/10971

import sys
input = sys.stdin.readline

n = int(input())
road_list = []
for i in range(n):
    road = list(map(int, input().split()))
    road_list.append(road)
visited = [0] * n
result = float('inf') # 무한대로 초기화 하는 이유 - 최소값을 찾는거니깐!

def dfs(start, now, value, cnt):
    global result

    if cnt == n:
        if road_list[now][start]:
            value = value + road_list[now][start]
            if result > value:
                result = value

    if value > result:
        return
    
    for i in range(n):
        if not visited[i] and road_list[now][i]:
            visited[i] = 1
            dfs(start, i, value + road_list[now][i], cnt + 1)
            visited[i] = 0

for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0

print(result)
