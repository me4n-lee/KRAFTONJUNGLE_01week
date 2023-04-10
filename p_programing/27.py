#https://www.acmicpc.net/problem/2628
#종이자르기
#2628

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
line = int(input())
wid = [0] * line #가로
leng = [0] * line #세로
max_big = 0

#가로로자르면세로 / 세로로자르면가로
for i in range(line):
    x, y = map(int, input().split())

    if x == 0:
        leng.append(y)
    else:
        wid.append(y)

wid.sort()
wid.append(a)
leng.sort()
leng.append(b)

max_wid = wid[0]
for i in range(1, len(wid)):
    max_wid = max(max_wid, wid[i] - wid[i-1])

max_leng = leng[0]
for i in range(1, len(leng)):
    max_leng = max(max_leng, leng[i] - leng[i-1])

result = max_wid * max_leng
print(result)

#     if x == 0:
#         leng[i] = y
#     # else:
#     #     wid[i] = y

#     if x == 1:
#         wid[i] = y

# # print(wid)
# #가로
# wid.sort()
# # print(wid)
# for i in range(line):
#     big = abs(wid[i] - wid[i-1])
#     if big > max_big:
#         max_big = big
    
# max_wid = max(wid)# 배열중 최대값
# min_wid = min(wid)# 배열중 최소값
# wid_max = max(min_wid,a-max_wid, max_big)
# # print(max_big)
# # print(wid_max)

# # print(leng)
# #가로
# leng.sort()
# for i in range(line):
#     big = abs(leng[i] - leng[i-1])
#     if big > max_big:
#         max_big = big
    
# max_leng = max(leng)# 배열중 최대값
# min_leng = min(leng)# 배열중 최소값
# leng_max = max(min_leng,b-max_leng, max_big)
# # print(max_big)
# # print(leng_max)

# result = wid_max * leng_max

# print(result)