#https://www.acmicpc.net/problem/2739
#구구단
#2739

import sys
input = sys.stdin.readline

a = int(input())

for i in range(1,10):
    result = a*i
    print(a, "*", i, "=", result)