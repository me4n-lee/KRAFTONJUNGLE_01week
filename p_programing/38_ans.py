# https://www.acmicpc.net/problem/10971
# 외판원 순회 2
# 10971

import sys
input = sys.stdin.readline

n = int(input())
city_road = []
for _ in range(n):
    a = list(map(int, input().split()))
    city_road.append(a)

ans = float('INF') # 최소값을 구하는 과정이기에, 무한대값을 집어넣어준다
visited = [0] * n

def dfs(start, now, road_sum, cnt):
    global ans

    if cnt == n:
        if city_road[now][start]:
            road_sum += city_road[now][start]
            if ans > road_sum:
                ans = road_sum
        return

    #각 탐색에서의 탈출조건 / 합의 값이 커진다면 빠져나갈 수 있어야함
    #백트래킹(가지치기)
    if road_sum > ans:
        return

    for i in range(n):
        if not visited[i] and city_road[now][i]:
            visited[i] = 1
            dfs(start, i, road_sum + city_road[now][i], cnt + 1)
            # value = value + city_road[now][i]
            # dfs(start, i, value, cnt + 1)
            # 이 방법을 안쓰는 이유는, 벨류값이 갱신되며 원래의 벨류값을 다른곳에 또 저장해야하는 번거로운 과정이 생기기 때문이다.
            visited[i] = 0

# print(city_road)

for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0

print(ans)