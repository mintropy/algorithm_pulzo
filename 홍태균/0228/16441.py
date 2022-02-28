'''
아기돼지와 늑대

'''
import sys

input = sys.stdin.readline

N, M = map(int,input().split())

dirs = [(-1,0),(0,1),(1,0),(0,-1)]
# 맵
maps = []
# 늑대 위치
wolfs = []

for i in range(N):
    sub_map = list(input().strip())
    # 늑대 위치 저장
    for j in range(M):
        if sub_map[j] == 'W':
            wolfs.append((i,j))
    maps.append(sub_map)

visit = [[0] * M for _ in range(N)]

# 탐색
def dfs(wolf):
    q = [wolf]
    
    while q:
        now = q.pop()
        visit[now[0]][now[1]] = 1
        
        for dir in dirs:
            next_x = now[0] + dir[0]
            next_y = now[1] + dir[1]
            # 다음 장소가 범위안의 방문 안한 곳인지
            if 0 <= next_x < N and 0 <= next_y < M and visit[next_x][next_y] == 0:
                # 초원이 나오면 해당 장소를 저장하고 
                # 답 도출을 위해 다른 모양으로 바꿔주고
                # 방문으로 변경
                if maps[next_x][next_y] == '.':
                    q.append((next_x,next_y))
                    maps[next_x][next_y] = ','
                    visit[next_x][next_y] = 1
                # 빙판의 경우
                elif maps[next_x][next_y] == '+':
                    # 빙판이 아닌게 나올 때 까지 이동
                    while maps[next_x][next_y] == '+':
                        next_x += dir[0]
                        next_y += dir[1]
                    # 그 장소가 산이라면
                    if maps[next_x][next_y] == '#':
                        # 그 전 장소가 방문한 적이 있는지 확인
                        # 방문한 적이 없으면 저장
                        # 방문으로 변경
                        if visit[next_x - dir[0]][next_y - dir[1]] == 0:
                            q.append((next_x - dir[0],next_y - dir[1]))
                            visit[next_x- dir[0]][next_y- dir[1]] = 1
                    # 초원이고 방문을 안했다면
                    # 저장
                    elif maps[next_x][next_y] == '.' and visit[next_x][next_y] == 0:
                        q.append((next_x,next_y))
                        maps[next_x][next_y] = ','
                        visit[next_x][next_y] = 1
    

for wolf in wolfs:
    dfs(wolf)

# 늑대가 이동한 초원은 , => . 
# 늑대가 못 가는 초원은 . => P
for i in range(N):
    for j in range(M):
        if maps[i][j] == ',':
            maps[i][j] = '.'
        elif maps[i][j] == '.':
            maps[i][j] = 'P'

for m in maps:
    print(''.join(m))
                
        

