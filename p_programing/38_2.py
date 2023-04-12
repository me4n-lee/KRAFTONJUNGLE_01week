import sys
# input = sys.stdin.readline

n = int(input())
city_list = []
for i in range(n):
    a = list(map(int, input().split()))
    city_list.append(a)

result = float('inf')  # 최소 비용을 저장하는 변수

def dfs(start, now, cnt, road_sum):
    global result

    if cnt == n:
        if city_list[now][start] != 0:
            result = min(result, road_sum + city_list[now][start])
        return

    for i in range(n):
        if not visited[i] and city_list[now][i] != 0:
            visited[i] = True
            road_sum += city_list[now][i]
            if road_sum < result:  # 가지치기
                dfs(start, i, cnt + 1, road_sum)
            visited[i] = False
            road_sum -= city_list[now][i]

for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(i, i, 1, 0)

print(result)
