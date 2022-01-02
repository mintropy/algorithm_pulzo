'''
경로 게임

'''
import sys
input = sys.stdin.readline

N = int(input())

maps = []
maps.append(list(input().strip()))
maps.append(list(input().strip()))

dirs = [(-1,0),(1,0),(0,1)]

# 탐색
def bfs(n):
    # 위아래 2번 방문하기 때문에 초기화
    visit = [[0] * N for _ in range(2)]

    # 검은 색이라면 100으로 리턴
    if maps[n[0]][n[1]] != '.':
        return 100

    # 탐색 시작 visit는 거리
    q = [n]
    visit[n[0]][n[1]] = 1

    while q:
        node = q.pop()
        # 끝에 도착하면 해당 거리 리턴
        if node[1] == N - 1:
            return visit[node[0]][node[1]]

        for dir in dirs:
            nx = node[0] + dir[0]
            ny = node[1] + dir[1]
            # 범위 안이고 방문 안했으며 흰색 길인거
            if 0<= nx < 2 and ny < N and visit[nx][ny] == 0 and maps[nx][ny] == '.':
                # 거리 증가
                visit[nx][ny] = visit[node[0]][node[1]] + 1
                q.append((nx,ny))

# 위와 아래중 거리가 짧은 거
route = min(bfs((0,0)),bfs((1,0)))
# 총 흰 길 중에서 짧은 거리의 흰 길을 빼면 지울 수 있는 길
total = maps[0].count('.') + maps[1].count('.') - route

print(total)