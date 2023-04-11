#https://www.acmicpc.net/problem/2562
#최댓값
#2562

import sys
input = sys.stdin.readline

n_list = []
for i in range(9):
    n = int(input())
    n_list.append(n)

# print(n_list)

def fun():
    global result_num, result_i
    max_num = 0

    for i in range(9):
        if n_list[i] > max_num:
            max_num = n_list[i]
            result_i = i + 1
        # if n_list[i] <= max_num:
        #     result_num = n_list[i]
        #     result_i = i

    print(max_num)
    print(result_i)
    
    return 

fun()