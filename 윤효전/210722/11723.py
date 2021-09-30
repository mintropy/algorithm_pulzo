import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

M = int(input())
s = set()
for _ in range(M):
    com = list(map(lambda x:x.rstrip(), input().split()))
    if len(com) == 1:
        if com[0] == 'all':
            s = {i for i in range(1, 21)}
        else:
            s.clear()
    else:
        com, x = com
        x = int(x)
        if com == 'add':
            s.add(x)
        elif com == 'check':
            print(1 if x in s else 0)
        elif com == 'remove':
            s.discard(x)
        elif com == 'toggle':
            s.discard(x) if x in s else s.add(x)