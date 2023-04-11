#https://www.acmicpc.net/problem/9663
#N-Queen
#9663
import sys
input = sys.stdin.readline

n = int(input())
row = [0] * n

def check(x, row):
    for i in range(x): 
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x, n, row):
    result = 0

    if n == 1:
        return 1
    elif n == 2 or n == 3:
        return 0
    
    if x == n:
        return 1
    else:
        for i in range(n):
            row[x] = i
            if check(x, row):
                result = result + dfs(x + 1, n, row)

    return result

print(dfs(0, n, row))