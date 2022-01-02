'''
미세먼지 안녕!

'''
import sys
input = sys.stdin.readline

R, C, T = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(R)]

# 공기 청정기 위치 찾기
for i in range(R):
    if maps[i][0] == -1:
        up_air_c = i
        down_air_c = i + 1
        break

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

# 확산
def diffusion():
    # 확산된 새로운 맵을 구현
    # 이렇게 하지 않으면 옆에서 확산한 먼지가 또 확산 될 수 있기 때문
    newmaps = [[0] * C for _ in range(R)]
    # 공기 청정기
    newmaps[up_air_c][0] = -1
    newmaps[down_air_c][0] = -1

    # 한 칸씩 확산
    for i in range(R):
        for j in range(C):
            # 먼지가 있을 때
            if maps[i][j] > 0:
                # 4칸중에 몇칸이 있는 확인하기 위해서
                cnt = 0
                # 퍼지는 양
                difdust = maps[i][j]//5
                for dir in dirs:
                    ni = i + dir[0]
                    nj = j + dir[1]
                    # 범위안이고 공기청정기가 없을 때
                    if 0 <= ni < R and 0 <= nj < C and maps[ni][nj] != -1:
                        cnt += 1
                        newmaps[ni][nj] += difdust
                # 확산한만큼 줄이기
                newmaps[i][j] += maps[i][j] - difdust * cnt
                
    return newmaps

# 공기청정기 위 순환
def up():
    # 한칸 위에서 시작
    x, y = up_air_c - 1, 0
    # 방향이 위, 왼쪽, 아래, 오른쪽 일정하기 때문에
    # 처음엔 위로 이동
    dir = [-1,0]
    # 공기 청정기 위에 도착하면 종료
    while x != up_air_c or y != 1:
        # 다음 위치
        nx, ny = x + dir[0], y + dir[1]
        # 맨 위에 도착하면 방향 전환
        if nx < 0:
            dir = [0,1]
        # 맨 오른쪽 도착하면 방향 전환
        elif ny == C:
            dir = [1,0]
        # 공기청정기 위쪽 라인에 도착하면 방향 전환
        elif nx > up_air_c:
            dir = [0,-1]
        # 해당 위치에 다음 위치의 먼지를 가지고 온다
        maps[x][y] = maps[x + dir[0]][y + dir[1]]
        # 다음 위치로 이동
        x += dir[0]
        y += dir[1]
    # 공기청정기옆은 0으로 초기화
    maps[x][y] = 0

def down():
    x, y = down_air_c + 1, 0
    dir = [1,0]
    while x != down_air_c or y != 1:
        nx, ny = x + dir[0], y + dir[1]
        if nx == R:
            dir = [0,1]
        elif ny == C:
            dir = [-1,0]
        elif nx < down_air_c:
            dir = [0,-1]
        maps[x][y] = maps[x + dir[0]][y + dir[1]]
        x += dir[0]
        y += dir[1]
    maps[x][y] = 0

# 시간만큼 해당 과정을 반복
for _ in range(T):
    maps = diffusion()
    up()
    down()
    
# 공기청정기가 -1이기 때문에 2를 더해주고 각 먼지를 합한다.
total = 2
for i in maps:
    total += sum(i)

print(total)