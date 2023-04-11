#https://www.acmicpc.net/problem/10819
#차이를 최대로
#10819

import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

# sum = 0
result = 0

perms = list(permutations(a))
#모든 배열을 섞어서 모든 경우의수의 순서를 가진 배열을 출력하는 함수

#배열 하나씩 확인해가며 찾아내야함
#뭐를? 차이의 값이 최대가 되는(절대값)

# for i in range(1부터 모든 배열의 개수):
    
#     sum = sum + abs(a[i] - a[i-1])

for a_list in perms:
    sum = 0 # 여기서 초기화를 해주야함 왜냐면 배열마다 반복돌리고 있으니깐
    for j in range(1, len(a_list)):
        sum = sum + abs(a_list[j] - a_list[j-1])

    result = max(result, sum)

print(result)
