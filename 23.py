#https://www.acmicpc.net/problem/2869
#달팽이는 올라가고 싶다
#2869

import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

result = 0 #
day = 0

# while result <= v:
#      day += 1
#      result = result + a
#      if result >=v:
#           break
#      else:
#         result = result - b
#     #  print(day)

day = ((v-a) / (a-b)) +1
result = int(day)

# if day == result:
#     print(result)
# else:
#     print(result+1)

if day%1 == 0 :
    print(int(day))
else:
    print(int(day+1))


#해당 코드에서 while문의 조건식인 result >= v에서 result의 초기값이 0이기 때문에 조건식이 거짓(False)이 되어 반복문이 실행되지 않습니다. 따라서 day의 초기값인 0이 그대로 출력되게 됩니다.