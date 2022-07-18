'''
놀이공원

'''
from sys import stdin
input = stdin.readline

N = int(input())

rides = [(600,600),(1320,1320)]

for _ in range(N):
    st, ed = input().split()
    st_h, st_m = map(int,[st[:2],st[2:]])
    ed_h, ed_m = map(int,[ed[:2],ed[2:]])
    st_t = st_h * 60 + st_m - 10
    ed_t = ed_h * 60 + ed_m + 10
    rides.append((st_t, ed_t))


rides.sort(key=lambda x:(x[0],x[1]))

time = 600
max_rest = 0

for st, ed in rides:
    if time < st:
        max_rest = max(max_rest,st-time)
    time = max(time,ed)

print(max_rest)