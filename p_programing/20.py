#https://www.acmicpc.net/problem/2675
#문자열 반복

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    r, s = input().split()
    case = list(map(str, str(s).strip()))
    x = int(r)

    for j in range(len(case)):
        for k in range(x):
           print(case[j], end="")
    
    #print()
    #print(case)



