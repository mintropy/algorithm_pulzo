import sys
input = sys.stdin.readline
M, N, L = map(int, input().split())
point = sorted(list(map(int, input().split())))
cnt = 0
def check(tx, th, x):
    if abs(tx - x) + th <= L:
        return True
    else:
        return False

def BS(target, height, s, e):
    global cnt
    if s >= e:
        if check(target, height, point[s]):
            cnt += 1
        elif s > 0 and check(target, height, point[s - 1]):
            cnt += 1
        elif s < M - 1 and check(target, height, point[s + 1]):
            cnt += 1
        return
    m = (s + e) // 2
    if point[m] == target:
        cnt += 1
        return
    elif point[m] < target:
        BS(target, height, m + 1, e)
    else:
        BS(target, height, s, m - 1)

for _ in range(N):
    x, y = map(int, input().split())
    if y > L:
        continue
    BS(x, y, 0, M - 1)
print(cnt)