import sys
import collections
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

pos = [-1] * 100001

def bfs(N, K):
    dq = collections.deque()
    dq.append(N)
    step = 0
    pos[N] = step
    while dq:
        cur = dq.popleft()
        step = pos[cur]
        next = [cur+1, cur-1, cur*2]
        for v in next:
            if 0 <= v <= 100000 and pos[v] == -1:
                dq.append(v)
                pos[v] = step + 1
    return pos[K]

print(bfs(N, K))