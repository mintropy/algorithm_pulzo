'''
나의 인생에는 수학과 함께

'''
import sys
input = sys.stdin.readline

N = int(input())

maps = [list(input().split()) for _ in range(N)]

def dfs(x,y,s):
    global max_s, min_s

    # 3개가 쌓이면(숫자2개와 연산1개) 계산하여 다시 새로 리스트에 넣는다.
    if len(s) == 3:
        s = [str(eval("".join(s)))]
    
    # 마지막에 도착하면 연산한 것을 최소, 최대를 판단한다.
    if x == N - 1 and y == N - 1:
        s = int(s[0])
        if max_s < s:
            max_s = s
        if min_s > s:
            min_s = s
        return
    # 탐색
    for dir in [(0,1),(1,0)]:
        nx = x + dir[0]
        ny = y + dir[1]
        # 범위 내에 존재하면 해당문자를 넣고 다시 dfs
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx,ny,s+[maps[nx][ny]])


max_s = -10000
min_s = 10000
dfs(0,0,[maps[0][0]])

print(max_s,min_s)

