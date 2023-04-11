#https://www.acmicpc.net/problem/1152
#단어의 개수
#1152

import sys
input = sys.stdin.readline

n = input()

def fun(n):
    split = n.split()
    result = len(split)

    return print(result)

fun(n)