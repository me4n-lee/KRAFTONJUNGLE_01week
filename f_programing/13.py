#https://www.acmicpc.net/problem/10871
#X보다 작은 수
#10871

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a_list = list(map(int, input().split()))

def fun(n):
    global result

    for i in range(n):
        if a_list[i] < x:
            print(a_list[i], end=" ")
    
fun(n)