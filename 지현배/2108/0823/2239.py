import sys
input = sys.stdin.readline
def DFS(n):
    # 종료 조건
    if n >= len(targets):
        return True
    # 확인할 좌표
    ni, nj = targets[n]
    for num in range(1, 10):
        # 해당 좌표의 행, 열, 스퀘어에 같은 숫자가 있는지 확인
        if not(ch_y[ni][num] or ch_x[nj][num] or ch_s[ni // 3 * 3 + nj // 3][num]):
            ch_y[ni][num] = ch_x[nj][num] = ch_s[ni // 3 * 3 + nj // 3][num] = True
            sudoku[ni][nj] = num
            # 종료 시 다음 탐색을 안하기 위해 계속 리턴함
            if DFS(n + 1) == True: return True
            sudoku[ni][nj] = 0
            ch_y[ni][num] = ch_x[nj][num] = ch_s[ni // 3 * 3 + nj // 3][num] = False
            
sudoku = [list(map(int, input().rstrip())) for _ in range(9)]
targets = []
# 해당 좌표의 행, 열, 스퀘어의 숫자가 있는지 확인 위한 배열
ch_y = [[False * 10] for _ in range(9)]
ch_x = [[False * 10] for _ in range(9)]
ch_s = [[False * 10] for _ in range(9)]
for i in range(9):
    for j in range(9):
        t = sudoku[i][j]
        # 해당 좌표가 0이면 탐색 리스트에 넣고
        if t == 0: targets.append([i, j])
        # 아니면 행, 열, 스퀘어에 표시한다
        else: ch_y[i][t] = ch_x[j][t] = ch_s[i // 3 * 3 + j // 3][t] = True
DFS(0)
for i in range(9):
    print(*sudoku[i], sep='')