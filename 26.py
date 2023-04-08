#https://www.acmicpc.net/problem/1065
#한수
#1065

import sys
input = sys.stdin.readline

n = int(input())
cnt =0
n_list = list(map(int, str(n)))
result = [] * len(n_list)

for i in range(1,len(n_list)+1):
    result[i] = n_list[i] - n_list[i-1] 

    if len(set(result[i])) == 1:
        cnt += 1
    

print(cnt)

    # if i<=99:
    #     cnt += 1

    # hun = int(i/100)
    # ten = int((i-(hun*100))/10)
    # one = n - (hun*100) - (ten*10)

    # if abs(hun-ten) == abs(ten-one):
    #     cnt += 1