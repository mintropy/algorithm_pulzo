'''
농장 관리

'''
import sys
input = sys.stdin.readline
N, M = map(int,input().split())

dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

maps = [list(map(int,input().split())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]

# 탐색
def dfs(i,j):
    q = [(i,j)]
    # 산봉우리면 1을 리턴하기 위해
    ans = 1
    # 높이 저장
    n = maps[i][j]

    while q:
        x, y = q.pop()

        visit[x][y] = 1

        for i in range(8):
            nx = x + dirs[i][0]
            ny = y + dirs[i][1]
            # 범위 파악
            if 0 <= nx < N and 0 <= ny < M:
                # 방문하지 않고 높이가 같으면 같은 봉우리이기 때문에 여기서도 탐색
                if maps[nx][ny] == n and visit[nx][ny] == 0:
                    q.append((nx,ny))
                # 만약 탐색중 더 높은 봉우리가 있다면 산봉우리가 아님
                elif maps[nx][ny] > n:
                    ans = 0
    return ans

# 결과
result = 0

# 전체를 탐색
for i in range(N):
    for j in range(M):
        # 방문하지 않았고 0 이상인 부분에서만 탐색
        if visit[i][j] == 0 and maps[i][j]:
            result += dfs(i,j)

print(result)

'''
8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 0 0
2 1 1 1 1 0 0
1 1 0 0 0 1 0
0 0 0 1 1 1 0
0 1 2 2 1 1 0
0 1 1 1 2 1 0

8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 1 0
2 1 1 1 1 0 0
1 1 0 0 0 1 0
0 0 0 1 1 1 0
0 1 2 2 1 1 0
0 1 1 1 2 1 0
'''