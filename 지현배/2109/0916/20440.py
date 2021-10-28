import sys
input = sys.stdin.readline
N = int(input())
arr = [[] for _ in range(2 * N)]
for i in range(N):
    Te, Tx = map(int, input().split())
    arr[2 * i] = (Te, 1)
    arr[2 * i + 1] = (Tx, 0)
arr.sort()
cV = 0
mV = 0
Tem = 0
Txm = 0
ismax = False
for i in range(2 * N):
    if arr[i][1] == 1:
        cV += 1
        if cV > mV:
            mV = cV
            ismax = True
            Tem = arr[i][0]
        elif cV == mV and Txm == arr[i][0]:
            ismax = True
    else:
        cV -= 1
        if ismax:
            ismax = False
            Txm = arr[i][0]
print(mV)
print(Tem, Txm)