'''
화산쇄설류

'''

import sys
input = sys.stdin.readline

M, N, V = map(int,input().split())
X, Y = map(int,input().split())
X -= 1
Y -= 1
maps = [list(map(int,input().split())) for _ in range(M)]
# 화산, 사람 방문 배열
vol_visit = [[0] * N for _ in range(M)]
per_visit = [[0] * N for _ in range(M)]

# 화산 시간에 따라 저장 200까지 하면 인덱스 에러 나오기 때문에
# 더크게 잡아야한다.
volcanos = [[] for _ in range(300)]
for _ in range(V):
    vol = list(map(int,input().split()))
    # 시간대에 
    volcanos[vol[2]].append([vol[0]-1,vol[1]-1])
    # 화산 위치는 움직일 수 없기 때문
    per_visit[vol[0]-1][vol[1]-1] = 1

# 사람 q
per_q = [[X,Y]]
# 답을 위해서 
max_h = maps[X][Y]
max_t = 0
# 시간
t = 0

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
# 탐색
while per_q:
    # 화산재 이동
    for vol_loc in volcanos[t]:
        # 방문시
        if vol_visit[vol_loc[0]][vol_loc[1]]:
            continue
        vol_visit[vol_loc[0]][vol_loc[1]] = 1
        # 이동
        for dir in dirs:
            next_vol_loc_x = vol_loc[0] + dir[0]
            next_vol_loc_y = vol_loc[1] + dir[1]

            if 0 <= next_vol_loc_x < M and 0 <= next_vol_loc_y < N:
                pass
            else:
                continue

            if vol_visit[next_vol_loc_x][next_vol_loc_y]:
                continue

            volcanos[t+1].append([next_vol_loc_x,next_vol_loc_y])
    
    # 사람 이동
    next_per_q = []
    for per_loc in per_q:
        # 방문과 화산
        if per_visit[per_loc[0]][per_loc[1]]:
            continue
        if vol_visit[per_loc[0]][per_loc[1]]:
            continue
        per_visit[per_loc[0]][per_loc[1]] = 1
        # 결과 확인
        if maps[per_loc[0]][per_loc[1]] > max_h:
            max_h = maps[per_loc[0]][per_loc[1]]
            max_t = t
        # 이동
        for dir in dirs:
            next_per_loc_x = per_loc[0] + dir[0]
            next_per_loc_y = per_loc[1] + dir[1]

            if 0 <= next_per_loc_x < M and 0 <= next_per_loc_y < N:
                pass
            else:
                continue
            if per_visit[next_per_loc_x][next_per_loc_y]:
                continue
            if vol_visit[next_per_loc_x][next_per_loc_y]:
                continue

            next_per_q.append([next_per_loc_x,next_per_loc_y])
            
    per_q = next_per_q[:]
    # 시간 증가
    t += 1

print(max_h,max_t)


