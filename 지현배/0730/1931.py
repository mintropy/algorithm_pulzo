'''
import sys
from operator import itemgetter

N = int(sys.stdin.readline())

session = []

for _ in range(N):
    session.append(list(map(int, sys.stdin.readline().split())))
session = sorted(session, key=itemgetter(1, 0))

cnt = 0
prev = 0
for s in session:
    if prev <= s[0]:
        cnt += 1
        prev = s[1]
print(cnt)

'''
import sys

N = int(sys.stdin.readline())

session = {}
idx_set = set()

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    idx_set.update([start, end])
    if start in session:
        session[start].append(end)
        session[start].sort()
    else:
        session[start] = [end]
idx_arr = sorted(list(idx_set))

prev = 0
res_dict = {}

for idx in idx_arr:
    if idx in res_dict:
        curr = res_dict[idx] = max(res_dict[idx], prev)
    else:
        curr = prev
    if idx in session:
        for next in session[idx]:
            if idx == next:
                curr += 1
                if idx in res_dict:
                    res_dict[idx] += 1
            elif next in res_dict:
                res_dict[next] = max(res_dict[next], curr + 1)
            else:
                res_dict[next] = curr + 1
    prev = curr
print(res_dict)
print(prev)