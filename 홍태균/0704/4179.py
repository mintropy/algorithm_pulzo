'''
불!

'''
def pprint(list_):
    for sub_ in list_:
        print(sub_)

from sys import stdin
input = stdin.readline

R, C = map(int,input().split())

maps = []
visit = [[0]*C for _ in range(R)] 
fires = []

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

# 초기화 작업
# 불, 지훈이 위치
for i in range(R):
    sub = list(input().strip())

    if "J" in sub:
        index = sub.index("J")
        J_idx = (i,index,0)
        visit[i][index] = 1
    
    for j in range(C):
        if "F" == sub[j]:
            fires.append((i,j))
    
    maps.append(sub)

q = [J_idx]

answer = -1

# 너비 탐색
def bfs():
    global answer, q, fires
    # 민규 위치
    while q:
        # 불 이동
        next_fires = []
        while fires:
            fire = fires.pop()
            for dir in dirs:

                if 0 <= fire[0]+dir[0] < R and 0 <= fire[1]+dir[1] < C:

                    if maps[fire[0]+dir[0]][fire[1]+dir[1]] == ["#","F"]:
                        continue
                    elif maps[fire[0]+dir[0]][fire[1]+dir[1]] in ["J","."]:
                        maps[fire[0]+dir[0]][fire[1]+dir[1]] = "F"
                        next_fires.append([fire[0]+dir[0],fire[1]+dir[1]])

        fires = next_fires[:]

        # 민규 이동
        next_q = []
        while q:
            now_x, now_y, cnt = q.pop()
            # 가장 자리 도착
            if now_x in [0,R-1] or now_y in [0,C-1]:
                answer = cnt
                return

            for dir in dirs:

                if 0 <= now_x+dir[0] < R and 0 <= now_y+dir[1] < C:

                    if visit[now_x+dir[0]][now_y+dir[1]]:
                        continue

                    if maps[now_x+dir[0]][now_y+dir[1]] == ["#","F"]:
                        continue
                    elif maps[now_x+dir[0]][now_y+dir[1]] == ".":
                        maps[now_x+dir[0]][now_y+dir[1]] = "J"
                        next_q.append([now_x+dir[0],now_y+dir[1],cnt+1])
                        visit[now_x+dir[0]][now_y+dir[1]] = cnt + 1

        q = next_q[:]

bfs()

if answer != -1:
    print(answer+1)
else:
    print("IMPOSSIBLE")


'''

4 6
######
......
#.J###
#F####

5

5 5
....F
...J#
....#
....#
...#.

4

3 3
F.F
.J.
F.F

I

4 4
####
JF.#
#..#
#..#

1
'''