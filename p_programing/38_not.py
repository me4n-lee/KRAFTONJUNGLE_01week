# 백준 10971번: 외판원 순회 2
# https://www.acmicpc.net/problem/10971

import sys
input = sys.stdin.readline

n = int(input())
city_list = []
for i in range(n):
    a = list(map(int,input().split()))
    city_list.append(a)
road_sum = 0 #모든 거리의 합
result = 0 #합중 최소를 저장하는곳

print(city_list)
print(city_list[1][0])

# city_list[i][j]

def dfs(start, now, cnt):
    # 만약 지금이 4번째 도시면, 스타트로 다시 돌아가고, 계산끝
    if cnt == n:
        road_sum = road_sum + city_list[][]
        return road_sum

    # 만약 road_sum 의 합이 result 값보다 작으면 result에 road_sum을 계속 넣으며,
    # 완전 탐색 해서 모든 road_sum끼리를 비교한뒤
    # 가장 작은값을 result 에 저장

    # i 도시에서 다음도시로 간다 치면,
    #     city_list[i] 중에서 가장 작은값 찾아야함
    if cnt < n:
        for i in range(len(city_list)):
            for j in range(len(city_list[i])):
            # road_sum 에 길이 추가 city_list[i][j]
                if road_sum
                    road_sum = road_sum +city_list
                    dfs(start, now, cnt+1)

for i in range(n):
    visited = [False]* n
    visited[i] = True
    dfs(i,i,)