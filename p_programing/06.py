#https://www.acmicpc.net/problem/2588
#곱셈
#2588

import sys
input = sys.stdin.readline

a= int(input())
b= int(input())

c = b%100

one = c%10
ten = int((c-one)/10)
hun = int((b-c)/100)

# print(one)
# print(ten)
# print(hun)

print(a*one)
print(a*ten)
print(a*hun)
print(a*b)