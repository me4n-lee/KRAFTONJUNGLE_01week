#https://www.acmicpc.net/problem/1110
#더하기 사이클
#1110

import sys
input = sys.stdin.readline

n = int(input())

n_2 = 0

if n < 10:
    n_2 = n * 10
else:
    n_2 = n
    
ten = n_2//10
one = n_2%10
new = 0
cnt = 0

# for i in range(100):
#     # new = (one*10) + (first%10)
#     # cnt += 1
#     if new != n_2:
#         new = (one*10) + (first%10)
#         cnt += 1
#         ten = new//10
#         one = new%10
#     else:
#         print(cnt)

while True:
    first = ten + one
    new = (one*10) + (first%10)
    cnt += 1

    if new == n_2:
        break

    ten = new // 10
    one = new % 10
    
print(cnt)