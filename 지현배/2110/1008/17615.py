import sys
input = sys.stdin.readline
def sol():
    N = int(input())
    balls = list(input().rstrip())
    # 공 개수
    rcnt = balls.count('R')
    bcnt = balls.count('B')
    # 한 공만 있다면 0
    if not rcnt or not bcnt:
        return 0
    # 양극단에서 연속적인 공의 개수 찾기
    l = balls[0]
    lcon = 1
    r = balls[-1]
    rcon = 1
    for i in range(1, N):
        if l != balls[i]:
            break
        lcon += 1
    for i in range(N - 2, -1, -1):
        if r != balls[i]:
            break
        rcon += 1
    # 경우의 수
    ans = N
    # 공을 왼쪽으로 모으는 경우
    if l == 'B':
        ans = min(ans, bcnt - lcon)
    else:
        ans = min(ans, rcnt - lcon)
    # 공을 오른쪽으로 모으는 경우
    if r == 'B':
        ans = min(ans, bcnt - rcon)
    else:
        ans = min(ans, rcnt - rcon)
    # 양극단에 위치한 공이 아니더라도 수가 적다면
    if rcnt < bcnt:
        ans = min(ans, rcnt)
    elif rcnt > bcnt:
        ans = min(ans, bcnt)
    return ans

print(sol())