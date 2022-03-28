import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = list(input().rstrip() for _ in range(N))

ans = 0
flag = False


def check_perfect(tmp):
    global ans, flag
    # 완전 제곱 수인지
    tmp = tmp.replace(' ', '')
    if tmp:
        is_perfect_jegop = int(tmp) ** (0.5)
        if is_perfect_jegop == int(is_perfect_jegop):
            if int(tmp) == is_perfect_jegop ** 2:
                ans = max(ans, int(tmp))
                flag = True


for si in range(N):  # 열 등차 수열에서 시작하는 수
    for di in range(-N, N):  # 열 등차 수열에서 간격
        for sj in range(M):  # 행 등차 수열에서 시작하는 수
            for dj in range(-M, M):  # 행 등차 수열에서의 간격

                tmp = ''
                if di == 0 and dj == 0:  # 둘 다 공차가 0이면 안됨
                    continue

                i = si
                j = sj
                while 0 <= i < N and 0 <= j < M:
                    tmp += board[i][j]
                    i += di
                    j += dj
                    check_perfect(tmp)

if flag:
    print(ans)
else:
    print(-1)
