#https://www.acmicpc.net/problem/10819
#차이를 최대로
#10819


def generate_permutations(arr, n, depth, used, current, result):
    if depth == n:
        result.append(current[:])
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            current.append(arr[i])
            generate_permutations(arr, n, depth + 1, used, current, result)
            current.pop()
            used[i] = False

n = int(input())
n_list = list(map(int, input().split()))

# 순열을 저장할 리스트
permutations = []
used = [False] * n
generate_permutations(n_list, n, 0, used, [], permutations)

max_sum = 0
for perm in permutations:
    sum_perm = sum(abs(perm[i] - perm[i - 1]) for i in range(1, n))
    # 차이 합계가 최대인 경우를 찾습니다.
    if sum_perm > max_sum:
        max_sum = sum_perm

print(max_sum)

# import sys
# input = sys.stdin.readline

# n = int(input())
# n_list = list(map(int, input().split()))

# min_list = sorted(n_list)
# max_list = sorted(n_list, reverse=True) # 내림차순
# result = []

# print(n_list)
# print(min_list)
# print(max_list)

# for i in range(n):
#     result.append(min_list[i])
#     result.append(max_list[i])

# print(result)

# sum_result = 0

# for i in range(1,n):
#     print(i)
#     sum_result = sum_result + abs(result[i]-result[i-1])

# print(sum_result)