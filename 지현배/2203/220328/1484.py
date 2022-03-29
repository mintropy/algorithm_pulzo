import sys
input = sys.stdin.readline

G = int(input())
curr = []
c = int(G ** 0.5)

while True:
    c += 1
    if c ** 2 - (c - 1) ** 2 > G:
        break
    gap = c ** 2 - G
    g = gap ** 0.5
    if g == int(g):
        curr.append(c)

if len(curr) > 0:
    print(*curr, sep='\n')
else:
    print(-1)