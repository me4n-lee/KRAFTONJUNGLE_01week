#https://www.acmicpc.net/problem/4344
#평균은 넘겠지

import sys
input = sys.stdin.readline

# average = [0] * 1000

c = int(input())
for i in range(c):
    n = list(map(int, input().split()))
    people = n[0]
    score = n[1:]

    average = sum(score)/people
    
    stu_cnt = 0

    for j in range(len(score)):
        if score[j] > average:
            stu_cnt += 1
    
    sub_result = (stu_cnt/len(score))*100

    result = "{:.3f}%".format(sub_result)


    print(result)

# for i in range(len(score)):
#     if score[i] > average