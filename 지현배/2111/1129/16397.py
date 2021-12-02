import sys
from collections import deque
input = sys.stdin.readline

N, T, G = map(int, input().split())
check = [True] * 100000
check[N] = False
queue = deque([[N, 0]])

ans = 'ANG'
while queue:
    num, cnt = queue.popleft()
    if cnt > T:
        break
    if num == G:
        ans = cnt
        break
    
    if num < 99999 and check[num + 1]:
        check[num + 1] = False
        queue.append([num + 1, cnt + 1])

    num *= 2
    if 0 < num < 100000:
        highest = 1
        if num >= 10000:
            highest = 10000
        elif num >= 1000:
            highest = 1000
        elif num >= 100:
            highest = 100
        elif num >= 10:
            highest = 10
        
        num -= highest
        if check[num]:
            check[num] = False
            queue.append([num, cnt + 1])
print(ans)