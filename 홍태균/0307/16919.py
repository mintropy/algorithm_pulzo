'''
봄버맨 2

'''
import sys

input = sys.stdin.readline

R, C, N = map(int,input().split())

maps = [list(input().strip()) for _ in range(R)]

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

bombs = []

# step3 폭탄 깔기
def step3():
    for i in range(R):
        for j in range(C):
            if maps[i][j] == '.':
                maps[i][j] = 'O'
            else:
                bombs.append((i,j))

# step4 폭발
def step4():
    while 1:
        # 폭탄이 없으면 돌아간다.
        if bombs:
            pass
        else:
            return
        # 폭탄을 터뜨리고 주위에도 터뜨리는 과정
        bomb = bombs.pop()
        maps[bomb[0]][bomb[1]] = '.'
        for dir in dirs:
            x = bomb[0] + dir[0]
            y = bomb[1] + dir[1]
            if 0 <= x < R and 0 <= y < C:
                maps[x][y] = '.'

# N 분기
# N = 1
if N == 1:
    pass        
else:
    N -= 1
    # 4로 나누어서 N을 줄인다.
    # 총 3단계 짝수, 4n+1, 4n+3
    # 그래서 4로 나눈 나머지로 N을 줄였다.
    N %= 4
    if N == 0:
        N = 4
    while 1:
        step3()
        N -= 1
        if N == 0:
            break
        
        step4()
        # 폭탄 초기화
        bombs = []
        N -= 1
        if N == 0:
            break
        
    
for line in maps:
    print("".join(line))