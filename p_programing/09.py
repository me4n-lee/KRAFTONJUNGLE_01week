#https://www.acmicpc.net/problem/1085
#직사각형에서 탈출
#1085

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

# print(x)
# print(y)
# print(w)
# print(h)

print(min(x,y,w-x,h-y))