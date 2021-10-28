import sys
from collections import deque
input = sys.stdin.readline
def sol():
    N, M = map(int, input().split())
    before = [list(map(int, input().split())) for _ in range(N)]
    after = [list(map(int, input().split())) for _ in range(N)]
    # before - after = difference
    difference = []
    for i in range(N):
        diff = []
        for j in range(M):
            diff.append(before[i][j] - after[i][j])
        difference.append(diff)
    # difference의 영역이 before의 영역 두 개 이상을 침범하는지 확인하기 위한 변수
    life = 1
    q = deque()
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    for i in range(N):
        for j in range(M):
            if difference[i][j] != 0:
                # life가 0이라는 것은 영역이 두 개 이상이라는 것
                if life == 0:
                    return 'NO'
                life -= 1
                # before 영역을 탐색하기 위한 befo_target
                # before 영역 내에서 다른 difference 영역이 있는지 탐색하기 위한 diff_target
                befo_target = before[i][j]
                diff_target = difference[i][j]
                q.append([i, j, diff_target])
                while q:
                    y, x, target = q.popleft()
                    # before 영역 내에 다른 difference가 있다는 것은
                    # 그 before 영역이 온전히 변하지 않았다는 것
                    if target != diff_target:
                        return 'NO'
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        # befo_target과 같은 영역만을 탐색
                        if 0 <= ny < N and 0 <= nx < M and before[ny][nx] == befo_target:
                            q.append([ny, nx, difference[ny][nx]])
                            # before는 다시 방문하지 않기 위해 0으로
                            # difference는 다음 탐색에 걸리지 않도록 0으로
                            before[ny][nx] = 0
                            difference[ny][nx] = 0
    return 'YES'
print(sol())