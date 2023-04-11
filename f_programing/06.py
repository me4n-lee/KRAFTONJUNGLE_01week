#https://www.acmicpc.net/problem/2588
#곱셈

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

def fun(x,y):
    global hun, ten, one
    global three, four, five, six

    hun = y // 100
    ten = (y-hun*100) // 10
    one = y % 10

    # return print(hun, ten, one)

    three = x * one
    four = x * ten
    five = x * hun
    six = x * y

    print(three)
    print(four)
    print(five)
    print(six)

    return

    # return three, four, five, six

fun(a,b)


