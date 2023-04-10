#https://www.acmicpc.net/problem/10872
#팩토리얼
#10872

import sys
input = sys.stdin.readline

n = int(input())
result = 0

def fact(n):
    if n == 0 or n == 1 :
        result = 1
    else:
        result = n * fact(n-1)
    return result

# def fact(n):
#     if n == 0 or n == 1 :
#         return 1
#     else:
#         return n * fact(n-1)
#     # return result

# print(fact(10))

print(fact(n))