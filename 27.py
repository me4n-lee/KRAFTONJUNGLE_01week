#https://www.acmicpc.net/problem/2628
#종이자르기
#2628

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
line = int(input())
# case = [] * line
# cross = [] * line
# cut = [] * line
wid = [0] * line #가로
leng = [0] * line #세로
max_big = 0

#가로로자르면세로 / 세로로자르면가로
for i in range(line):
    x, y = map(int, input().split())

    if x == 0:
        leng[i] = y
    # else:
    #     wid[i] = y

    if x == 1:
        wid[i] = y


print(wid)
#가로
for i in range(line):
    big = abs(wid[i] - wid[i-1])
    if big > max_big:
        max_big = big



chai = max(abs(a-wid[i]),wid[i], max_big)


print(chai)

    


# print(leng)


# print(case)
# print(cross)
# print(cut)