# 백준 10971번: 외판원 순회 2
# https://www.acmicpc.net/problem/10971

import sys
input = sys.stdin.readline

n = int(input())
city_list = []
for i in range(n):
    a = list(map(int,input().split()))
    city_list.append(a)

print(city_list)
print(city_list[1][0])

# city_list[i][j]

def dfs(cnt):
    global start, now

    # 만약 지금이 4번째 도시면, 스타트로 다시 돌아가고, 계산끝
    if cnt == n:
        road_sum = road_sum + city_list[][]
        return

    # i 도시에서 다음도시로 간다 치면,
    #     city_list[i] 중에서 가장 작은값 찾아야함
    
    if cnt < n:
        for i in range(len(city_list)):
            for j in range(len(city_list[i])):
            # road_sum 에 길이 추가 city_list[1][2]
            dfs(cnt+1)

dfs(0)