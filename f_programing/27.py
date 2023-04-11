#https://www.acmicpc.net/problem/2628
#종이자르기
#2628

import sys
input = sys.stdin.readline

def calculate_max_area(a, b, line, cuts):
    wid = [0]
    leng = [0]
    
    for x, y in cuts:
        if x == 0:
            leng.append(y)
        else:
            wid.append(y)

    wid.sort()
    wid.append(a)
    leng.sort()
    leng.append(b)

    max_wid = max(wid[i] - wid[i-1] for i in range(1, len(wid)))
    max_leng = max(leng[i] - leng[i-1] for i in range(1, len(leng)))

    return max_wid * max_leng

a, b = map(int, input().split())
line = int(input())
cuts = [tuple(map(int, input().split())) for _ in range(line)]
result = calculate_max_area(a, b, line, cuts)
print(result)