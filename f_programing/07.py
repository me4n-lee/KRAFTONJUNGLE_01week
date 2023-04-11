#https://www.acmicpc.net/problem/9498
#시험 성적
#9498

import sys
input = sys.stdin.readline

score = int(input())

def fun(score):
    if score >= 90:
        return print("A")
    elif score >= 80:
        return print("B")
    elif score >= 70:
        return print("C")
    elif score >= 60:
        return print("D")
    else:
        return print("F")
    
fun(score)