import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(lambda x:(x[0], int(x[1])), enumerate(input().split(), 1)))
S.sort(key=lambda x:x[1], reverse=True)

if S[0][1] > (N+1)/2:
    print(-1)
    exit(0)

dq = deque(S)
ans = [0] * N

pos = 0
end = False
while dq:
    color, cnt = dq.popleft()
    
    while pos < len(ans) and cnt > 0 and not end:
        ans[pos] = color
        if cnt == 1:
            pos += 1
        else:
            pos += 2
            
        cnt -= 1
        
        if pos >= len(ans):
            end = True
            pos = 0
            break
        
    if end:
        while pos < len(ans) and cnt > 0:
            if ans[pos] == 0:
                ans[pos] = color
                cnt -= 1
            pos += 1
        
        
print(*ans)