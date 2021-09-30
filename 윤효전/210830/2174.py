from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def command(num, cmd, cnt):
    dl = ('N', 'W', 'S', 'E')
    dr = ('N', 'E', 'S', 'W')
    d_pos = {'N': (1, 0), 'S': (-1, 0), 'E': (0, 1), 'W': (0, -1)}

    y = robot_list[num]['y']
    x = robot_list[num]['x']
    robot = board[y][x]

    if cmd == 'L':
        tmpd = dl.index(robot[1])
        robot[1] = dl[(tmpd + cnt) % 4]
    elif cmd == 'R':
        tmpd = dr.index(robot[1])
        robot[1] = dr[(tmpd + cnt) % 4]
    else:
        dy, dx = d_pos[robot[1]]
        tmp_y, tmp_x = y, x
        for _ in range(cnt):
            tmp_y += dy
            tmp_x += dx
            if tmp_y < 1 or tmp_y > R or tmp_x < 1 or tmp_x > C:
                print(f'Robot {robot[0]} crashes into the wall')
                # pprint(board)
                # pprint(robot_list)
                exit()
            if board[tmp_y][tmp_x] != None:
                print(
                    f'Robot {robot[0]} crashes into robot {board[tmp_y][tmp_x][0]}')
                # pprint(board)
                # pprint(robot_list)
                exit()
        board[tmp_y][tmp_x] = robot
        board[y][x] = None
        robot_list[num]['y'] = tmp_y
        robot_list[num]['x'] = tmp_x


C, R = map(int, input().split())
board = [[None]*(C+1) for _ in range(R+1)]

N, M = map(int, input().split())

robot_list = {i: {'y': None, 'x': None} for i in range(1, N+1)}
for i in range(1, N+1):
    x, y, dirc = input().rstrip().split()
    x = int(x)
    y = int(y)
    board[y][x] = [i, dirc]
    robot_list[i]['y'] = y
    robot_list[i]['x'] = x

# pprint(board)
# pprint(robot_list)

for _ in range(M):
    num, cmd, cnt = input().rstrip().split()
    num = int(num)
    cnt = int(cnt)
    command(num, cmd, cnt)

print(f'OK')
pprint(board)
pprint(robot_list)
