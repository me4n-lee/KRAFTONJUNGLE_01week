#https://www.acmicpc.net/problem/10869
#사칙연산

import sys
input = sys.stdin.readline

A, B = input().split()
 
a = int(A)
b = int(B)

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)