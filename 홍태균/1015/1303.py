'''
전쟁 - 전투

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

num_list = [list(input()) for _ in range(M)]

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

# 위치, 색깔
def bfs(x,y,C):
    global cnt_W, cnt_B

    q = [(x,y,C)]
    # 다른 아무 문자로 visit 역할을 대신
    num_list[x][y] = "A"

    # 카운트는 현재부터 시작하기 때문에 1로 시작
    cnt = 1

    # bfs 시작
    while q:
        i,j,C = q.pop(0)
        # 탐색
        for dir in dirs:
            ni = i + dir[0]
            nj = j + dir[1]
            # 범위안에서 같은 색이면
            if 0<= ni < M and 0 <= nj < N and num_list[ni][nj] == C:
                q.append((ni,nj,C))
                num_list[ni][nj] = "A"
                # 연결된 병사 증가
                cnt += 1
    # 그 색에 카운트를 제곱해서 증가
    if C == "W":
        cnt_W += cnt ** 2
    else:
        cnt_B += cnt ** 2


cnt_W = 0
cnt_B = 0
# 모든 곳을 탐색
for i in range(M):
    for j in range(N):
        # 그 색에 맞게 bfs
        if num_list[i][j] == "W":
            bfs(i,j,"W")
        elif num_list[i][j] == "B":
            bfs(i,j,"B")

print(cnt_W,cnt_B)