#https://www.acmicpc.net/problem/8958
#OX퀴즈

import sys
input = sys.stdin.readline


n = int(input())

for i in range(n):
    case = list(input().strip())

    sub_result = [0] * len(case)

    if case[0] == 'O':
        sub_result[0] = 1
    else:
        sub_result[0] = 0

    for i in range(n):
        for j in range(1, len(case)):
            if case[j] == 'O':
                sub_result[j] = sub_result[j-1] + 1
            else:
                sub_result[j] = 0

    print(sum(sub_result))
    
# for i in range(n):
#     print(sub_result)

    # elif case[i] == 'X':
    #     result += 0