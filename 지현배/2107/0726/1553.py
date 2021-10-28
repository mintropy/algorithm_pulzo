import sys
grid = []
for _ in range(8):
    grid.append(sys.stdin.readline().rstrip())
dominos = [
    '00', '01', '02', '03', '04', '05', '06',
    '11', '12', '13', '14', '15', '16',
    '22', '23', '24', '25', '26',
    '33', '34', '35', '36',
    '44', '45', '46',
    '55', '56',
    '66'
]
# 도미노가 놓여있으면 1 아니면 0
check = [[0 for _ in range(7)] for _ in range(8)]
# 경우의 수 카운트
count = 0
def DFS(idx):
    # 종료조건 - 끝 노드에 도달하면 카운트를 한다.
    if idx >= 28:
        global count
        count += 1
        return
    # 모든 격자 순회
    for i in range(8):
        for j in range(7):
            # 격자와 도미노의 한 부분이 일치하고 격자가 비어있으면 진입
            if grid[i][j] == dominos[idx][0] and check[i][j] == 0:
                # 방명록 남김
                check[i][j] = 1
                # 도미노 나머지 부분도 검사
                if i > 0 and grid[i - 1][j] == dominos[idx][1]\
                    and check[i - 1][j] == 0:
                    check[i - 1][j] = 1
                    DFS(idx + 1)
                    check[i - 1][j] = 0
                if j < 6 and grid[i][j + 1] == dominos[idx][1]\
                    and check[i][j + 1] == 0:
                    check[i][j + 1] = 1
                    DFS(idx + 1)
                    check[i][j + 1] = 0
                check[i][j] = 0
                # 도미노 두 부분이 같은 숫자가 아닐경우 진입
                if not dominos[idx][0] == dominos[idx][1]:
                    if i < 7 and grid[i + 1][j] == dominos[idx][1]\
                        and check[i + 1][j] == 0:
                        check[i + 1][j] = 1
                        DFS(idx + 1)
                        check[i + 1][j] = 0
                    if j > 0 and grid[i][j - 1] == dominos[idx][1]\
                        and check[i][j - 1] == 0:
                        check[i][j - 1] = 1
                        DFS(idx + 1)
                        check[i][j - 1] = 0
DFS(0)
print(count)