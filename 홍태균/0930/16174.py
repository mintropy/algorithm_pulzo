'''
점프왕 쩰리 (Large)

'''
import sys
input = sys.stdin.readline

N = int(input())

maps = [list(map(int,input().split())) for _ in range(N)]
# 방문
visit = [[0] * N for _ in range(N)]
# 방향
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

i = j = 0
# DFS
def dfs(r,c):
    stack = [(r,c)]
    # 방문
    visit[r][c] = 1
    while stack:
        i,j = stack.pop()
        # 4방향 탐색
        for dir in dirs:
            # 현재 위치의 이동수만큼 곱해서 다음 좌표 찾기
            nr = i + maps[i][j]*dir[0]
            nc = j + maps[i][j]*dir[1]
            # 해당 좌표 끝 좌표인가
            if nr == N - 1 and nc == N - 1:
                print("HaruHaru")
                return
            # 해당 좌표가 범위 내에 있고 방문을 안했는가
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
                stack.append((nr,nc))
                visit[nr][nc] = 1
    # 다 돌았는데 못가면
    print("Hing")
    return

dfs(0,0)

