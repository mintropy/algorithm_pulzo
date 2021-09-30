import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    start, end = map(int, input().split())
    l.append((start, end))
l.sort(key=lambda x:(x[1], x[0]))
#print(l)

cnt = 0
last_one = (-1, -1)
for start, end in l:
    if last_one[1] <= start:
        last_one = start, end
        cnt += 1
        #print(start, end)

print(cnt)
