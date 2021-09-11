import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(10)]
res = -1
# 남은 색종이 개수
amount = [0, 5, 5, 5, 5, 5]
# 범위를 벗어나거나 구간 내에 0이 있는지 확인
def check(y, x, n):
    if y + n >= 11 or x + n >= 11: return False
    for i in range(y, y + n):
        for j in range(x, x + n):
            if arr[i][j] == 0:
                return False
    return True
# 구간 내의 수를 t(0 or 1)로 바꿈
def change(y, x, n, t):
    for i in range(y, y + n):
        for j in range(x, x + n):
            arr[i][j] = t
def sol(n, cnt):
    global res
    # 가지치기
    if res != -1 and cnt >= res:
        return
    # 종료조건
    if n >= 100:
        if res == -1 or res > cnt:
            res = cnt
        return
    y = n // 10
    x = n % 10
    if arr[y][x] == 1:
        for k in range(5, 0, -1):
            if check(y, x, k) and amount[k] > 0:
                amount[k] -= 1
                change(y, x, k, 0)
                sol(n + k, cnt + 1)
                amount[k] += 1
                change(y, x, k, 1)
    else:
        sol(n + 1, cnt)
sol(0, 0)
print(res)


