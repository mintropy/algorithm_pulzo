from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

board = [(9,)*21] + [(9,) + tuple(map(int, input().split())) + (9,)
                     for _ in range(19)] + [(9,)*21]

# for v in board:
#     print(v)


def make_dirs(y, x):
    dy = (0, 1, 1, 1)
    dx = (1, 0, 1, -1)
    ret = []
    for i in range(4):
        tmp_list = []
        tmp_y, tmp_x = y, x
        tmp_list.append((tmp_y, tmp_x))
        for _ in range(6):
            tmp_y += dy[i]
            tmp_x += dx[i]
            if tmp_y < 0 or tmp_y >= 21 or tmp_x < 0 or tmp_x >= 21:
                break
            tmp_list.append((tmp_y, tmp_x))
        else:
            ret.append(tmp_list)

    return ret


print(make_dirs(1, 1))


def chk_board(target, dir):
    for i in range(len(dir)):
        pos_list = []
        for j in range(len(dir[i])):
            y, x = dir[i][j]
            if j == 0 or j == 6:
                if board[y][x] != target:
                    continue
                else:
                    break
            else:
                if board[y][x] == target:
                    pos_list.append((y, x))
                    continue
                else:
                    break
        else:
            pos_list.sort(key=lambda x: (x[1], x[0]))
            return pos_list[0]

    return None


def chk():
    ret = None
    for i in range(21):
        for j in range(21):
            dirs = make_dirs(i, j)
            for k in range(1, 3):
                ret = chk_board(k, dirs)
                if ret != None:
                    return k, ret


ans = chk()
if ans == None:
    print(0)
else:
    print(ans[0])
    print(*ans[1])
