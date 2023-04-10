#https://www.acmicpc.net/problem/10869
#사칙연산
#10869

import sys
input = sys.stdin.readline

a,b = map(int, input().split())

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def divide(a, b):
    return int(a / b)

def remain(a, b):
    return a % b

print(plus(a,b))
print(minus(a,b))
print(mult(a,b))
print(divide(a,b))
print(remain(a,b))