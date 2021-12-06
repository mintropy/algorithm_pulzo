def solution(board, aloc, bloc):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    # 세로, 가로의 길이
    n, m = len(board), len(board[0])
    
    def dfs(turn, aloc, bloc):
        nonlocal board, dx, dy, n, m
        # turn 인 차례의 플레이어의 네 방향 확인
        moves = []
        for d in range(4):
            if turn == 'a':
                x, y = aloc[0] + dx[d], aloc[1] + dy[d]
            else:
                x, y = bloc[0] + dx[d], bloc[1] + dy[d]
            if 0 <= x < n and 0 <= y < m:
                # 해당 칸으로 이동 할 수 있을 때
                if board[x][y]:
                    # 만약 a, b가 같은 장소에 있었다면 moves에만 추가
                    if aloc == bloc:
                        moves.append(1)
                    else:
                        if turn == 'a':
                            board[aloc[0]][aloc[1]] = 0
                            moves.append(dfs('b', [x, y], bloc))
                            board[aloc[0]][aloc[1]] = 1
                        else:
                            board[bloc[0]][bloc[1]] = 0
                            moves.append(dfs('a', aloc, [x, y]))
                            board[bloc[0]][bloc[1]] = 1
        if not moves:
            return 0
        else:
            return max(moves) + 1
    
    return dfs('a', aloc, bloc)
