import collections
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, S, D, F, B, K = map(int, input().split())
K_list = map(int, input().split())
visit = [-1]*(N+1)

for n in K_list:
    visit[n] = -2


dq = collections.deque()
dq.append((S, 0))
while dq:
    target, t = dq.popleft()
    if 0 < target <= N and visit[target] == -1:
        #print(target, t)
        visit[target] = t
        if target == D:
            break
        dq.append((target+F, t+1))
        dq.append((target-B, t+1))

ans = visit[D]
if ans == -1:
    print('BUG FOUND')
else:
    print(ans)
