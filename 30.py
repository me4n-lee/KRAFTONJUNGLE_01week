#https://www.acmicpc.net/problem/9663
#N-Queen
#9663

import sys
input = sys.stdin.readline

n = int(input())

def queen():
    if n == 1:
        return 1
    