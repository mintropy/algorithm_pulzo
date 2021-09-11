def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    arr = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for sk in skill:
        typ, r1, c1, r2, c2, degree = sk
        sign = 1
        if typ == 1: sign = -1
        arr[r1][c1] += degree * sign
        arr[r1][c2 + 1] += degree * -sign
        arr[r2 + 1][c1] += degree * -sign
        arr[r2 + 1][c2 + 1] += degree * sign
    for i in range(N):
        cnt = 0
        for j in range(M):
            cnt += arr[i][j]
            arr[i][j] = cnt
    for j in range(M):
        cnt = 0
        for i in range(N):
            cnt += arr[i][j]
            board[i][j] += cnt
            if (board[i][j] > 0): answer += 1
    return answer