#https://www.acmicpc.net/problem/1085
#직사각형에서 탈출
#1085

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

def fun(x, y, w, h):
    global result

    result = min(x, y, w-x, h-y)

    return print(result)

fun(x, y, w, h)