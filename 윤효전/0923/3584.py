import collections
import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline


def make_tree(N):
    ret = {i: {'parent': [0]*LOG, 'depth': None, 'to': []}
           for i in range(1, N+1)}
    for _ in range(N-1):
        A, B = map(int, input().split())
        ret[B]['parent'][0] = A
        ret[A]['to'].append(B)
    return ret


def setParent(tr):
    for j in range(1, LOG):
        for i in range(1, N+1):
            tmp = tr[i]['parent'][j-1]
            if tmp:
                tr[i]['parent'][j] = tr[tmp]['parent'][j-1]


def find_root(tr):
    for i in range(1, N+1):
        if tr[i]['parent'][0] == 0:
            return i


def cal_depth(tr):
    dq = collections.deque()
    dq.append(ROOT)
    tr[ROOT]['depth'] = 0
    while dq:
        tmp = dq.popleft()
        for node in tr[tmp]['to']:
            dq.append(node)
            tr[node]['depth'] = tr[tmp]['depth'] + 1


def find_LCA(tr, A, B):
    if tr[A]['depth'] < tr[B]['depth']:
        A, B = B, A

    for i in range(LOG-1, -1, -1):
        if tr[A]['depth'] - tr[B]['depth'] >= (1 << i):
            A = tr[A]['parent'][i]

    if A == B:
        return A

    for i in range(LOG-1, -1, -1):
        if tr[A]['parent'][i] != tr[B]['parent'][i]:
            A = tr[A]['parent'][i]
            B = tr[B]['parent'][i]

    return tr[A]['parent'][0]


LOG = 14
ROOT = None
T = int(input())
for _ in range(T):
    N = int(input())
    tr = make_tree(N)
    setParent(tr)
    ROOT = find_root(tr)
    cal_depth(tr)
    A, B = map(int, input().split())
    lca = find_LCA(tr, A, B)
    print(lca)
    # pprint(tr)
