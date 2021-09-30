from pprint import pprint
import collections
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def make_tree(N):
    ret = {i: {'data': 0, 'to': []} for i in range(1, N+1)}
    S = tuple(map(int, input().split()))
    for i in range(1, N):
        ret[S[i]]['to'].append(i+1)
    return ret


def bfs(tr, node):
    dq = collections.deque()
    dq.append((node, 0))
    while dq:
        i, w = dq.popleft()
        tr[i]['data'] += w
        for next in tr[i]['to']:
            dq.append((next, tr[i]['data']))


ROOT = 1
N, M = map(int, input().split())
tr = make_tree(N)
for _ in range(M):
    i, w = map(int, input().split())
    tr[i]['data'] += w

bfs(tr, ROOT)
pprint(tr)

print(*[tr[i]['data'] for i in range(1, N+1)])
