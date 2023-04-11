#https://www.acmicpc.net/problem/1065
#한수
#1065

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

def is_hansu(num):
    num_list = list(map(int, str(num)))
    if len(num_list) <= 2:
        return True
    diffs = [num_list[i] - num_list[i-1] for i in range(1, len(num_list))]
    return len(set(diffs)) == 1

for i in range(1, n+1):
    if is_hansu(i):
        cnt += 1

print(cnt)