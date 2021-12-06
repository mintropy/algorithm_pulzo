'''
Title : 도미노 찾기
Link : https://www.acmicpc.net/problem/1553
'''

import sys

input = sys.stdin.readline

# sys.setrecursionlimit(int(1e6))

def dfs(i, j, visited, domino_used):
    global domino_board, count, check
    # 백트래킹 종료 조건 확인
    # 놓은 도미노가 28개일 때
    if check == 28:
        count += 1
        return
    # 가로 범위를 벗어나면, 그 다음줄 탐색
    elif j == 7:
        i += 1
        j = 0
    # 이미 탐색한 칸이면 오른쪽 칸으로 이동하여 탐색
    # 밑으로 탐색하는 경우가 있어, 넘어가야 하는 경우 발생
    if visited[i][j]:
        dfs(i, j + 1, visited, domino_used)
        return
    # i, j 위치에서 오른쪽, 밑으로 확인
    # 오른쪽 확인
    # 좌우로 놓을 때, 오른쪽 칸에 놓을 수 잇는지 확인
    if j <= 5 and not visited[i][j + 1]:
        # 해당 하는 칸의 숫자를 확인, 도미노 사용할 수 있는지 확인
        num1 = domino_board[i][j]
        num2 = domino_board[i][j + 1]
        # 사용한 도미노 확인을 위해, 항상 num2가 크거나 같게
        if num1 > num2:
            num1, num2 = num2, num1
        if not domino_used[num1][num2]:
            # 사용하지 않았으면 사용 처리
            visited[i][j] = True
            visited[i][j + 1] = True
            domino_used[num1][num2] = True
            check += 1
            # 오른쪽 한 칸을 확인했으니, 오른쪽 두 칸 이동 후 탐색
            dfs(i, j + 2, visited, domino_used)
            check -= 1
            visited[i][j] = False
            visited[i][j + 1] = False
            domino_used[num1][num2] = False
    # 밑으로 확인
    if i <= 6:
        # 해당 하는 칸의 숫자를 확인, 도미노 사용할 수 있는지 확인
        num1 = domino_board[i][j]
        num2 = domino_board[i + 1][j]
        # 사용한 도미노 확인을 위해, 항상 num2가 크거나 같게
        if num1 > num2:
            num1, num2 = num2, num1
        if not domino_used[num1][num2]:
            # 사용하지 않았으면 사용 처리
            visited[i][j] = True
            visited[i + 1][j] = True
            domino_used[num1][num2] = True
            check += 1
            # 밑으로 탐색했으니, 오른쪽 한칸 이동 후 탐색
            dfs(i, j + 1, visited, domino_used)
            check -= 1
            visited[i][j] = False
            visited[i + 1][j] = False
            domino_used[num1][num2] = False


domino_board = [[int(i) for i in input().strip()] for _ in range(8)]
# 각 위치를 방문한지 확인
visited = [[False for _ in range(7)] for _ in range(8)]

# 사용한 도미노 확인
# 도미노 확인은 오른쪽 삼각형 부분만 확인(중복되는 도미노 확인 X)
# 항상 domino_used[i][j]에서 i <= j인 경우만 확인
domino_used = [[False for _ in range(7)] for _ in range(7)]
# 경우의 수
count = 0
# 도미노를 놓은 개수
check = 0

dfs(0, 0, visited, domino_used)
print(count)