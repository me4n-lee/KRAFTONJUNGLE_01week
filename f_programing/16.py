#https://www.acmicpc.net/problem/4344
#평균은 넘겠지

import sys
input = sys.stdin.readline

c = int(input())

def fun(score, people):
    cnt = 0

    average = sum(score) / people

    for i in range(len(score)):
        if score[i] > average:
            cnt += 1
    
    sub_result = cnt / people * 100
    result = "{:.3f}%".format(sub_result)
    
    return print(result)

for i in range(c):
    n = list(map(int, input().split()))
    people = n[0]
    score = n[1:]
    fun(score, people)
    # print(people)
    # print(score)