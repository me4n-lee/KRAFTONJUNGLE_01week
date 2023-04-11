#https://www.acmicpc.net/problem/1978
#소수 찾기
#1978

import sys
input = sys.stdin.readline

n = int(input())
case = list(map(int, input().split()))
cnt = 0

def fun(n):
    global cnt

    for i in range(n):
        if case[i] == 1:
            continue
        for j in range(2,int(case[i]**0.5)+1):
            if case[i]%j == 0:
                break
        else:
            cnt += 1

    return print(cnt)

fun(n)