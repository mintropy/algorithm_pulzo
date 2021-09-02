import sys
# 그냥 리스트로 큐를 구현하면 .pop(0)가 너무 오래걸려서 deque 사용
from collections import deque
ipt = sys.stdin.readline
def sol():
    M, N, H = map(int, ipt().split())
    box = []
    queue = deque()
    empty_cnt = 0
    rotten_cnt = 0
    # 입력을 받으면서 썩은 토마토 정보를 큐에 넣고 그 수를 카운트함
    # 비어있는 칸의 개수도 카운트함
    for h in range(H):
        temp = []
        for n in range(N):
            arr = list(map(int, ipt().split()))
            for m in range(M):
                if arr[m] == 1:
                    queue.append([0, h, n, m])
                    rotten_cnt += 1
                elif arr[m] == -1:
                    empty_cnt += 1
            temp.append(arr)
        box.append(temp)

    # 6 방향
    dy = [0, 0, 1, 0, -1, 0]
    dx = [0, 0, 0, 1, 0, -1]
    dz = [1, -1, 0, 0, 0, 0]

    res = 0
    while queue:
        # 큐에는 좌표와 그 좌표에 있는 토마토가 썩기까지 걸리는 날
        day, z, y, x = queue.popleft()
        for idx in range(6):
            ny = y + dy[idx]
            nx = x + dx[idx]
            nz = z + dz[idx]
            if 0 <= ny < N and 0 <= nx < M and 0 <= nz < H:
                # 토마토가 썩으면 1로 표시
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = 1
                    rotten_cnt += 1
                    queue.append([day + 1, nz, ny, nx])
                    res = max(res, day + 1)

    # 썩은 토마토 개수 + 비어있는 칸의 개수가 전체 칸보다 작으면 -1
    if M * N * H > rotten_cnt + empty_cnt:
        print(-1)
    else:
        print(day)
sol()