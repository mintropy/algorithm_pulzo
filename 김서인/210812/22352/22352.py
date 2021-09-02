import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
before_photo = list(list(map(int, input().split())) for _ in range(N))
after_photo = list(list(map(int, input().split())) for _ in range(N))

# 상우하좌, 해당 위치
di = [-1, 0, 1, 0, 0]
dj = [0, 1, 0, -1, 0]


def same():
    """
    전, 후 사진이 동일한지 체크하는 함수
    """
    for i in range(N):
        for j in range(M):
            if before_photo[i][j] != after_photo[i][j]:
                return False

    return True


# 동일하지 않은 부분 -> 같은 데이터 값이고 상하좌우로 인접한 부분 값이 다 바뀌었는지
def vaccine():
    """
    전, 후 사진에서 다른 부분을 만나면
    전 사진과 후 사진에서 그 부분, 상하좌우로 인접한 부분들 값을 다 -1로 바꿔준다.
    """
    Q = deque()
    change_cnt = 0  # 한 군데만 바뀌는지 체크하려고!!

    for i in range(N):
        for j in range(M):
            if before_photo[i][j] != after_photo[i][j]:
                before_val = before_photo[i][j]
                after_val = after_photo[i][j]
                Q.append((i, j))

                while Q:
                    y, x = Q.popleft()
                    # before_photo[y][x] = -1
                    # after_photo[y][x] = -1
                    for mode in range(5):

                        ni = y + di[mode]
                        nj = x + dj[mode]

                        # 같은 데이터 값이고, 상하좌우로 인접하면 그 부분 방문 처리
                        if 0 <= ni < N and 0 <= nj < M and before_photo[ni][nj] == before_val:
                            Q.append((ni, nj))
                            # 재방문하지 않도록
                            before_photo[ni][nj] = -1

                            if after_photo[ni][nj] == after_val:
                                # 재방문하지 않도록
                                after_photo[ni][nj] = -1

                return  # 한 군데만 백신 투여하게!


vaccine()
if same():
    print("YES")
else:
    print("NO")
