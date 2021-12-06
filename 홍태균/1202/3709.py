'''
레이저빔은 어디로

'''
import sys
input = sys.stdin.readline

T = int(input())

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

# 테스트케이스
# 그리고 안되는 경우는 없다.
for tc in range(T):
    n, r = map(int,input().split())

    # 맵 만들기
    maps = []
    for _ in range(n+2):
        maps.append([0] * (n+2))

    # 거울 설치
    for _ in range(r):
        x, y = map(int,input().split())
        maps[x][y] = 1

    # 레이저 위치
    start =list(map(int,input().split()))
    # 레이저 위치에 따라 방향 설정
    if start[0] == 0:
        pre_dir = 2
    elif start[1] == n + 1:
        pre_dir = 3
    elif start[0] == n + 1:
        pre_dir = 0
    elif start[1] == 0:
        pre_dir = 1
    
    # 반복을 위해서
    nx, ny = start[0], start[1]
    # 찾아다니기
    while 1:
        # 방향 따라 이동
        nx, ny = nx + dirs[pre_dir][0], ny + dirs[pre_dir][1]
        # 다음 위치가 끝에 도착했다면
        # 출력하고 끝
        if nx == 0 or nx == n + 1 or ny == 0 or ny == n + 1:
            print(nx,ny)
            break
        # 1 이면 방향 전환
        # 방향은 무조건 오른쪽으로 바뀌기 때문에
        # 0 -> 1 -> 2 -> 3 -> 0 으로 바뀐다.
        elif maps[nx][ny] == 1:
            pre_dir = (pre_dir + 1) % 4

'''
1
2 3
1 1
1 2
2 2
3 1
'''
