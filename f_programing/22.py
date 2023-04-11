#https://www.acmicpc.net/problem/2908
#상수
#2908

import sys
input = sys.stdin.readline

a,b = map(int, input().split())

def fun(a,b):
    reverse_a = str(a)[::-1]
    reverse_b = str(b)[::-1]

    if reverse_a > reverse_b:
        result = reverse_a
    elif reverse_a < reverse_b:
        result = reverse_b

    return print(result)

fun(a,b)