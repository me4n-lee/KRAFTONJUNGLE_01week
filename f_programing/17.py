#https://www.acmicpc.net/problem/2577
#숫자의 개수
#2577

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

# print(a)
# print(b)
# print(c)

def fun(a,b,c):
    global cnt_list

    mult = a * b * c
    mult_list = list(map(str, str(mult)))
    cnt_list = [0] * 10
    # print(mult_list)
    for i in range(len(mult_list)):
        for j in range(0,10):
            if mult_list[i] == str(j):
                cnt_list[j] += 1

    return cnt_list


for i in range(10):
    fun(a,b,c)
    print(cnt_list[i])
    
