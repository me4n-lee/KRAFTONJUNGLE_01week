#https://www.acmicpc.net/problem/10950
#A+B - 3
#10950

import sys
input = sys.stdin.readline

def fun(a,b):
    global result

    result = a + b

    return print(result)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    fun(a,b)