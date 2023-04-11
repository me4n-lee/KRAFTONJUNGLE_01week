#https://www.acmicpc.net/problem/8958
#OX퀴즈
#8958

import sys
input = sys.stdin.readline

n = int(input())

def fun(case):
    result = [0] * len(case)

    for i in range(len(case)):
        if case[i] == "O":
            result[i] += 1
            if i>0 and case[i-1] == "O":
                result[i] = result[i] + result[i-1]

        if case[i] == "X":
            result[i] = 0

    print(sum(result))

        
for i in range(n):
    case = list(input().strip())
    # print(case)
    fun(case)