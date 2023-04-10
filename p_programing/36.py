#https://www.acmicpc.net/problem/2309
#일곱 난쟁이
#2309

import sys
input = sys.stdin.readline

sum_short = 0
short_list = []
for i in range(9):
    short = int(input())
    short_list.append(short)

# print(short_list)
short_list.sort()

# print(short_list)
# print(sum(short_list))

chai = sum(short_list) - 100

for i in range(9):
    for j in range(9):
        if short_list[i] != short_list[j]:
            if short_list[i] + short_list[j] == chai:
                a = short_list[i]
                b = short_list[j]

for i in range(len(short_list)):
    if short_list[i] == a or short_list[i] == b:
        short_list[i] = 0
# print(short_list)

short_list = [x for x in short_list if x != 0] #0이 아닌것들만 출력할수 있는 수식! 알아둬야함!

for i in range(len(short_list)):
    print(short_list[i])
# for i in range(len(short_list)):
#     if sum_short < 100:
#         sum_short = sum_short + short_list[i]
#         print(sum_short)

#     if sum_short > 100:
#         sum_short = sum_short - short_list[i]


    