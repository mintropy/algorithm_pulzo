import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]

def chk(i):
    ret = 0
    if i < N:
        for j in range(N):
            ret += S[j][i]
    else:
        i %= N
        for j in range(N):
            ret += S[i][j]
    if ret > N//2:
        return 1
    else:
        return 0

def turn(i, n):
    if i < N:
        for j in range(N):
            S[j][i] = n
    else:
        i %= N
        for j in range(N):
            S[i][j] = n

visit = [0]*(N*2)

while True:
    sw = False
    for i in range(N*2):
        if visit[i] == 0 and chk(i) == M:
            visit[i] = 1
            turn(i, M)
            sw = True
    if sw == False:
        break

if all(visit):
    print(1)
else:
    print(0)