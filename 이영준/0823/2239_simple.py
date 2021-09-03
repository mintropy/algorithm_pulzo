"""
Title : 스도쿠
Link : https://www.acmicpc.net/problem/2239
"""

import sys
input = sys.stdin.readline


def solve_sudoku(n):
    global sudoku, sudoku_row, sudoku_col, sudoku_sq
    if n == 81:
        for line in sudoku:
            print(*line, sep = '')
        # return True
        exit()
    x, y = n // 9, n % 9
    if sudoku[x][y]:
        # return solve_sudoku(n + 1)
        solve_sudoku(n + 1)
    else:
        for i in range(1, 10):
            if not sudoku_row[x][i] and not sudoku_col[y][i] and not sudoku_sq[(x // 3) * 3 + y // 3][i]:
                sudoku_row[x][i] = sudoku_col[y][i] = sudoku_sq[(x // 3) * 3 + y // 3][i] = True
                sudoku[x][y] = i
                # if solve_sudoku(n + 1):
                #     return True
                solve_sudoku(n + 1)
                sudoku_row[x][i] = sudoku_col[y][i] = sudoku_sq[(x // 3) * 3 + y // 3][i] = False
                sudoku[x][y] = 0
    # return False


sudoku = [list(int(i) for i in input().strip()) for _ in range(9)]
sudoku_row = [[False] * 10 for _ in range(9)]
sudoku_col = [[False] * 10 for _ in range(9)]
sudoku_sq = [[False] * 10 for _ in range(9)]
for i, row in enumerate(sudoku):
    for j, m in enumerate(row):
        if m:
            sudoku_row[i][m] = True
            sudoku_col[j][m] = True
            sudoku_sq[(i // 3) * 3 + j // 3][m] = True

solve_sudoku(0)
