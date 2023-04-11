#https://www.acmicpc.net/problem/2869
#달팽이는 올라가고 싶다
#2869

import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

def fun():
    day = ((v-a)/(a-b)) + 1
    result = int(day)

    if day%1 == 0:
        print(result)
    else:
        print(result + 1)

fun()

# result = 0 #
# day = 0

# # while result <= v:
# #      day += 1
# #      result = result + a
# #      if result >=v:
# #           break
# #      else:
# #         result = result - b
# #     #  print(day)

# day = ((v-a) / (a-b)) +1
# result = int(day)

# # if day == result:
# #     print(result)
# # else:
# #     print(result+1)

# if day%1 == 0 :
#     print(int(day))
# else:
#     print(int(day+1))