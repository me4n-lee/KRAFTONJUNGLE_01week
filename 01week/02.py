#https://www.acmicpc.net/problem/9095
#1, 2, 3 더하기
#9095

import sys
input = sys.stdin.readline

t = int(input())

def fun(case):
    if case == 0:
        return 1
    if case < 0:
        return 0
    
    sum = fun(case-1) + fun(case-2) + fun(case-3)

    # return print(sum)
    return sum

for i in range(t):
    case = int(input())
    print(fun(case))