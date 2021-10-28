import sys
input = sys.stdin.readline
N = int(input())
arr = [input().split() for _ in range(N)]
maxV = -(5 ** N)
minV = 5 ** N
def DFS(y, x, oper):
    if y == N - 1 and x == N - 1:
        res = eval(oper)
        global maxV, minV
        maxV = max(maxV, res)
        minV = min(minV, res)
        return
    if (y + x) % 2 == 0:
        oper = str(eval(oper))
    if y + 1 < N:
        DFS(y + 1, x, oper + arr[y + 1][x])
    if x + 1 < N:
        DFS(y, x + 1, oper + arr[y][x + 1])
DFS(0, 0, arr[0][0])
print(maxV, minV)