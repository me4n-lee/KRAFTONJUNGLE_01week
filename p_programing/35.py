#https://www.acmicpc.net/problem/1181
#단어 정렬
#1181

import sys
input = sys.stdin.readline

n = int(input())
word_list = []
# word_leng = []
for i in range(n):
    word = input().strip()#/n제거
    word_list.append(word)

#print(word_list)
word_result = list(set(word_list)) # 중복 키값 제거
result = sorted(word_result, key=lambda x: (len(x), x)) # 키 두개로 정렬

for i in range(len(result)):
    print(result[i])
# word_list.sort()

# print(word_list)

# for i in range(n):
#     word_leng[i] = len(word_list[i]) -1
#     print(word_leng)

# word_leng.sort()
# print(word_result)