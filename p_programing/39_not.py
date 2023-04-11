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

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and not area_list[nx][ny] and area_list[nx][ny] > h:
            area_list[nx][ny] = True
            dfs(nx, ny, h)

ans = 1
for k in range(max(map(max, area_list))):
    visit = [[False]*n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if area_list[i][j] > k and not visit[i][j]:
                safe += 1
                visit[i][j] = True
                dfs(i, j, k)
    ans = max(ans, safe)

print(ans)