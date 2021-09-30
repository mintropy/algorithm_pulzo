import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def chk(startY, startX, endY, endX):
    tmp = S[startY][startX]
    for y in range(startY, endY+1):
        for x in range(startX, endX+1):
            if S[y][x] != tmp:
                return -1
    return tmp


def dc(startY, startX, endY, endX):
    if startY == endY and startX == endX:
        print(S[startY][startX], end='')
        return
    c = chk(startY, startX, endY, endX)
    if c == '0':
        print(c, end='')
        return
    elif c == '1':
        print(c, end='')
        return
    else:
        tp = (
            (startY, startX, (startY+endY)//2, (startX+endX)//2),
            (startY, (startX+endX)//2+1, (startY+endY)//2, endX),
            ((startY+endY)//2+1, startX, endY, (startX+endX)//2),
            ((startY+endY)//2+1, (startX+endX)//2+1, endY, endX)
        )
        print('(', end='')
        for v in tp:
            dc(v[0], v[1], v[2], v[3])
        print(')', end='')


N = int(input())
S = [input().rstrip() for _ in range(N)]

dc(0, 0, N-1, N-1)
