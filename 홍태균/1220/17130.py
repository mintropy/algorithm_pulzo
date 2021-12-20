'''
토끼가 정보섬에 올라온 이유

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

# 맵 만들기
maps = [list(input().strip()) for _ in range(N)]

# 토끼 위치 찾기
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'R':
            R = (i,j)

# DP 생성 및 초기화
dp = [[-1] * M for _ in range(N)]
dp[R[0]][R[1]] = 0

# 정답 저장
result = -1

# DP 탐색
# 열을 이동하기 때문에 열 부터 시작
# 토끼 해당 열에서 마지막 전까지
for j in range(R[1],M-1):
    for i in range(N):
        # 해당 위치에서 0이상이면 이동할 수 있는 것을 의미
        if dp[i][j] >= 0:
            # 9시 6시 3시 방향 이동
            for ni in [-1,0,1]:
                nexti = i + ni
                # 범위 안에 들어오는지
                if 0<= nexti < N:
                    # 벽일 때, -1로 유지
                    if maps[nexti][j+1] == '#':
                        continue
                    # 빈 공간일 때, 현재 값과 이동하기 전의 값을 비교
                    elif maps[nexti][j+1] == '.':
                        dp[nexti][j+1] = max(dp[nexti][j+1],dp[i][j])
                    # 당근일 때, 현재 값과 이동하기 전의 값 + 1 을 비교
                    elif maps[nexti][j+1] == 'C':
                        dp[nexti][j+1] = max(dp[nexti][j+1],dp[i][j] + 1)
                    # 쪽문일 때, 현재 값과 이동하기 전의 값을 비교
                    elif maps[nexti][j+1] == 'O':
                        dp[nexti][j+1] = max(dp[nexti][j+1],dp[i][j])
                        # 그리고 지금 결과값과 현재 값을 비교
                        if result < dp[i][j]:
                            result = dp[i][j]

print(result)


'''
2 4
CC..
RC##

10 10
..........
C.CCCCCCCC
..#.CC.C..
CCCCCC#CCC
.RC.CCCC..
..........
###.#####.
....CCCCCO
..........
..........

'''


