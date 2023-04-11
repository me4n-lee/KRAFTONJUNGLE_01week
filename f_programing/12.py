#https://www.acmicpc.net/problem/2438
#별 찍기 - 1
#2438

import sys
input = sys.stdin.readline

n = int(input())

def fun(n):
    global result

    for i in range(1,n+1):
        result = "*" * i
        print(result)

    return

fun(n)
        