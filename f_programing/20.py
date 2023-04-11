#https://www.acmicpc.net/problem/2675
#문자열 반복

import sys
input = sys.stdin.readline

t = int(input())

def fun(x, case):
    for j in range(len(case)):
        for k in range(x):
           print(case[j], end="")
    print()


for _ in range(int(t)):
    r, s = map(str, input().split())
    case = list(map(str, str(s).strip()))
    x = int(r)
    fun(x, case)

