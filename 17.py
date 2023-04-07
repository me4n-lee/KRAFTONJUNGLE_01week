#https://www.acmicpc.net/problem/2577
#숫자의 개수

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

mul = str(a*b*c)

#print(mul)
n = list(map(int, str(mul)))

#print(n)

result = [0] * 10

for i in range(len(n)):
    if n[i] == 0:
        result[0] +=1
    if n[i] == 1:
        result[1] +=1
    if n[i] == 2:
        result[2] +=1
    if n[i] == 3:
        result[3] +=1
    if n[i] == 4:
        result[4] +=1
    if n[i] == 5:
        result[5] +=1
    if n[i] == 6:
        result[6] +=1
    if n[i] == 7:
        result[7] +=1
    if n[i] == 8:
        result[8] +=1 
    if n[i] == 9:
        result[9] +=1
for i in range(len(result)):
    print(result[i])