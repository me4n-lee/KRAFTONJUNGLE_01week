#https://www.acmicpc.net/problem/1914
#하노이 탑
#1914

import sys
input = sys.stdin.readline

n = int(input())

def hanoi(n, a, b, c):
    if n == 1:
        print (a, c)
        return
    
    hanoi(n-1, a, c, b)
    print(a,c)
    hanoi(n-1, b, a, c)


print(2**n -1)
if n<=20:
    hanoi(n,1,2,3)