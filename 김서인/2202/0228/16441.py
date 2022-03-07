import sys, collections

input = sys.stdin.readline
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
board = list(input().rstrip() for _ in range(N))
wolve_can_go = list([False] * M for _ in range(N))
ans = []

# 늑대 사는 곳
wolve = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'W':
            wolve.append((i, j))

# 늑대 사는 곳에서 출발!
for wolf in wolve:
    i, j = wolf
    q = collections.deque()
    q.append((i, j))
    wolve_can_go[i][j] = True  # 출발 지점 방문 체크
    while q:
        ii, jj = q.popleft()

        for k in range(4):
            ni, nj = ii + direction[k][0], jj + direction[k][1]
            if 0 <= ni < N and 0 <= nj < M and wolve_can_go[ni][nj] == False:  # 범위, 방문 체크
                if board[ni][nj] == '#':  # 산
                    wolve_can_go[ni][nj] = True
                    continue
                elif board[ni][nj] == '.':  # 초원 = 여기에 돼지 못 산다.
                    wolve_can_go[ni][nj] = True
                    q.append((ni, nj))
                elif board[ni][nj] == '+':  # 빙판 => 쭉 그 방향으로 미끌어 져야 함!
                    idx = 1
                    while True:
                        nni, nnj = ii + direction[k][0] * idx, jj + direction[k][1] * idx
                        if 0 <= nni < N and 0 <= nnj < M:
                            if board[nni][nnj] == '+':  # 이것도 빙판이면 더 가기
                                idx += 1
                            elif board[nni][nnj] == '.' and wolve_can_go[nni][nnj] == False:  # 초원이라면 그만
                                wolve_can_go[nni][nnj] = True
                                q.append((nni, nnj))
                                break
                            elif board[nni][nnj] == '#' and wolve_can_go[nni - direction[k][0]][
                                nnj - direction[k][1]] == False:  # 산이라면 멈추기
                                wolve_can_go[nni - direction[k][0]][nnj - direction[k][1]] = True
                                q.append((nni - direction[k][0], nnj - direction[k][1]))
                                break
                            else:
                                break

                        else:  # 범위에 해당하지 않으면
                            break  # 그만!

for i in range(N):
    for j in range(M):
        if board[i][j] == '.' and not wolve_can_go[i][j]:
            print('P', end='')
        else:
            print(board[i][j], end='')
    print()
