from functools import cache
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [input().rstrip() for _ in range(N)]
calced = set()
answer = -1

def check(num):
    n = int(num)
    d = n ** 0.5
    if d == int(d):
        return True
    return False

for i in range(N):
    for j in range(M):
        num = table[i][j]
        if not num in calced:
            calced.add(num)
            if check(num):
                answer = max(answer, int(num))
        for y in range(N):
            for x in range(M):
                if y == i and x == j:
                    continue
                ny, nx = y, x
                n = num
                y_diff, x_diff = y - i, x - j
                while True:
                    if 0 <= ny < N and 0 <= nx < M:
                        n += table[ny][nx]
                        ny += y - i
                        nx += x - j
                        if not n in calced:
                            calced.add(n)
                            if check(n):
                                answer = max(answer, int(n))
                    else:
                        break;
print(answer)