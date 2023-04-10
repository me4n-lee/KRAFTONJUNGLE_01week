#https://www.acmicpc.net/problem/2908
#상수
#2908

import sys
input = sys.stdin.readline

a,b = map(int, input().split())

#문자열 뒤집기 (str(num)[::-1])
a_reverse = str(a)[::-1]
b_reverse = str(b)[::-1]

if a_reverse > b_reverse:
    print(a_reverse)
else:
    print(b_reverse)

#문자열 뒤집기 (str(num)[::-1])