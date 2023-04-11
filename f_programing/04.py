#https://www.acmicpc.net/problem/2557
#Hello World
#2557

# def fun():
#     a = "Hello World!"
#     return print(a)

# fun()

import sys
input = sys.stdin.readline

a,b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
elif a==b:
    print("==")