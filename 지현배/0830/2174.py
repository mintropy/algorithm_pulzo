import sys
input = sys.stdin.readline
A, B = map(int, input().split())
N, M = map(int, input().split())
ground = [[0 for _ in range(A + 2)] for _ in range(B + 2)]
drct = ((1, 0), (0, 1), (-1, 0), (0, -1))
drct_idx = ["N", "E", "S", "W"]
status = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    x, y, d = input().split()
    status[i] = [int(x), int(y), drct_idx.index(d)]
    ground[int(y)][int(x)] = i
command = [list(input().split()) for _  in range(M)]
isDone = False
for i in range(M):
    if isDone == True: break
    robo, com, cnt = command[i]
    robo, cnt = int(robo), int(cnt)
    x, y, d = status[robo]
    if com == 'F':
        while cnt:
            ny = y + drct[d][0]
            nx = x + drct[d][1]
            if 0 < ny <= B and 0 < nx <= A and ground[ny][nx] == 0:
                ground[ny][nx] = robo
                ground[y][x] = 0
                y = ny
                x = nx
                status[robo] = [x, y, d]
            else:
                if ground[ny][nx] != 0:
                    print(f"Robot {robo} crashes into robot {ground[ny][nx]}")
                else:
                    print(f"Robot {robo} crashes into the wall")
                isDone = True
                break
            cnt -= 1
    elif com == 'L':
        status[robo][2] = (d + 3 * cnt) % 4
    elif com == 'R':
        status[robo][2] = (d + cnt) % 4
if isDone == False:
    print("OK")