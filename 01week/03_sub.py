#https://www.acmicpc.net/problem/1182
#부분수열의 합
#1182

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
n_list = list(map(int, input().split()))
cnt = 0

# print(n_list)

def fun(n,result):
    global cnt

    # #만약 끝까지 갔는데 없으면 return
    # if n == len(n_list):
    #     return
    
    # #중간까지 가다가 합이 s랑 같아지면 cnt+=1 한다음 리턴
    # if result == s:
    #     cnt += 1
    #     return
    
    if n == len(n_list):
        return

    if result + n_list[n] == s:
        cnt += 1

    #재귀호출
    fun(n+1, result)
    fun(n+1, result + n_list[n])
    #b = 그 값을 더해서 진행하기 / a = 그 값을 빼고 진행하기 두가지

    # a = fun(n+1,result)
    # b = fun(n+1,result+n_list[n])

    # return a+b

# print(fun(0,0))

fun(0, 0)

#공집합!!
# if s == 0:
#     cnt -= 1

print(cnt)

    
# def fun(n):
#     for i in range(n):
#         sum += n_list[i]

#         if sum == s:
#             cnt += 1
#             return cnt
#         else:
#             #수열에 아직 넣지 않은 수를 더해준다
#             #이걸 끝날때까지 반복? 느낌으로 / 재귀함수로 구현하는 문제인것 같음 
#             #내 개인적인 생각으론 완전탐색에 가까움
    

#     return

# print(fun(0))