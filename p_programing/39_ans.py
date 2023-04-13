#https://www.acmicpc.net/problem/2468
#안전 영역
#2468

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
area_list = []
for i in range(n):
    area = list(map(int, input().split()))
    area_list.append(area)
state_sink = [[0] * n for _ in range(n)]
max_height = max(max(area_list))

#만약 내가 체크한 area_list[i][j]의 state_sink가 1이라면
#   cnt+=1
#그다음 area_list[i][j]의 state_sink = 0 으로 바꿈
#그다음 상하좌우 모두, 그리고 그 모두의 상하좌우의 state_sink를 확인해서 1이면 전부 0으로 바꿈

#이과정을 i*j 동안 반복

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, h, state_sink):
    state_sink[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and state_sink[nx][ny] == 1:
            dfs(nx, ny, h, state_sink)

max_cnt = 0
for h in range(max_height + 1):
    for i in range(n):
        for j in range(n):
            if h >= area_list[i][j]:
                state_sink[i][j] = 0
            else:
                state_sink[i][j] = 1

    cnt = 0

    for i in range(n):
        for j in range(n):
            if state_sink[i][j]:
                dfs(i,j,h,state_sink)
                cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)

#pypy3으로 제출해서 거의 1시간반을 해맴 python3으로 제출해야했음