'''
뱀

'''
import sys
input = sys.stdin.readline

def pprint(list):
    for i in list:
        print(*i)

# 맵 크기
N = int(input())
# 사과 수
K = int(input())
# 사과 위치
apples = [list(map(int,input().split())) for _ in range(K)]
# 방향 전환 수
L = int(input())
# 방향 전환을 딕셔너리로 생성
snakes = {}
for _ in range(L):
    x, c = input().split()
    x = int(x)
    snakes[x] = c

# 맵에 방향을 넣어주기(꼬리를 위해서)
# 사과 인덱스가 1,1로 시작하기 때문에 패딩 넣어주기
maps = [[[0,0] for _ in range(N+2)] for _ in range(N+2)]
# 사과 넣어주기
for i,j in apples:
    maps[i][j] = [2,0]
# 뱀 넣어주기
maps[1][1] = [1,0]

# 시간
cnt = 0
# 방향
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
# 처음 방향
dir = 0
# 머리와 꼬리 위치
tail = [1,1]
head = [1,1]
# 끝날때까지 무한 반복
while 1:
    # 시간 증가
    cnt += 1
    # 해당 방향으로 머리 이동
    head[0] += dirs[dir][0]
    head[1] += dirs[dir][1]

    # 머리가 맵에 있는가?
    if 0 < head[0] <= N and 0 < head[1] <= N:
        # 사과가 있는가? 있으면 패스
        if maps[head[0]][head[1]][0] == 2:
            pass
        # 뱀이 있으면 그만
        elif maps[head[0]][head[1]][0] == 1:
            break
        # 아무것도 없으면 꼬리 이동
        else:
            maps[tail[0]][tail[1]][0] = 0
            t_dir = maps[tail[0]][tail[1]][1]
            tail[0] += dirs[t_dir][0]
            tail[1] += dirs[t_dir][1]

        maps[head[0]][head[1]][0]= 1
        maps[head[0]][head[1]][1]= dir
    # 머리가 맵에 없으면 그만
    else:
        break

    # 해당 시간에 방향이 전환되는가?
    if cnt in snakes.keys():
        # 오른쪽이면 오른쪽 방향으로 아니면 왼쪽으로
        if snakes[cnt] == "D":
            dir = (dir + 1)%4
        else:
            dir = (dir - 1)%4
    
    # 머리에 방향 입력
    maps[head[0]][head[1]][1] = dir

print(cnt)
    
'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

'''


