import sys

input = sys.stdin.readline
MIISS = lambda: map(int, input().strip().split())
directions = [(0, -1), (1, -1), (-1, -1)]

N, M = MIISS()
arr = list(input().strip() for _ in range(N))
dp = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]


# 토끼가 들어온 위치 찾기
def find_a_rabbit_start():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                return (i, j)


ri, rj = find_a_rabbit_start()
side_doors = []
visited[ri][rj] = True

for j in range(rj + 1, M): # 왼쪽으로는 못 가니까 ri+1부터 보기
    for i in range(N):
        if arr[i][j] == '#':
            continue  # 벽이면 넘어가기

        # 그 지점으로 올 수 있는 세 지점 중 당근 수 젤 많은 것
        most_carrot_spot = 0
        flag = False # 그 지점까지 갈 수 있는지 체크

        for ki, kj in directions:
            ni, nj = i + ki, j + kj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]:
                # 그 지점으로 올 수 있는 세 지점 - 범위 체크, 방문한 적이 있어야 함! ( 다 벽이면 못 감)
                most_carrot_spot = max(most_carrot_spot, dp[ni][nj])
                flag = True

        if flag == False: # 다 벽이면 못가는데, 갈 수 있다는 뜻
            continue

        visited[i][j] = True # 그 지점에 갈 수 있다는 뜻이니까 방문 체크 !

        if arr[i][j] == 'C':
            dp[i][j] = most_carrot_spot + 1

        elif arr[i][j] == '.':
            dp[i][j] = most_carrot_spot

        elif arr[i][j] == 'O':
            if most_carrot_spot == -1:  # 여기까지 도달하지 못했으면
                continue
            dp[i][j] = most_carrot_spot
            side_doors.append(most_carrot_spot)

# 쪽문으로 나갈 수 있으면
if side_doors:
    print(max(side_doors))
else:  # 불가능
    print(-1)
