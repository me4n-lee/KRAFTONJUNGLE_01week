#https://www.acmicpc.net/problem/2739
#구구단
#2739

import sys
input = sys.stdin.readline

n = int(input())

def fun(n):
    global result

    for i in range(1,10):
        result = i * n
        print(n, "*", i, "=", result)

    return

fun(n)