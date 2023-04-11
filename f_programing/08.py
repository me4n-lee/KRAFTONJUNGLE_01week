#https://www.acmicpc.net/problem/2753
#윤년
#2753

import sys
input =sys.stdin.readline

n = int(input())

def fun(year):
    global result

    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        result = 1
    else:
        result = 0

    return print(result)

fun(n)