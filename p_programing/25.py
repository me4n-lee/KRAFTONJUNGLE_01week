#https://www.acmicpc.net/problem/9020
#골드바흐의 추측

t=int(input())
    

def decimal(a):
    if a == 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a%i == 0:
            return False
    return True

    
for i in range(t):
    n=int(input())
    for j in range(n//2, 0, -1):
        if decimal(n-j) and decimal(j):
            print(j, n-j)
            break




