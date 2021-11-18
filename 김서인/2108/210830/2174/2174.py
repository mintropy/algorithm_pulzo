import collections

direction_move_index = {'W': (0, -1), 'S': (1, 0), 'E': (0, 1), 'N': (-1, 0)}
r_direction = ['N', 'E', 'S', 'W']  # 오른쪽으로
l_direction = ['N', 'W', 'S', 'E']  # 왼쪽으로


def crash_wall(i, j):
    """
    범위 밖으로 가는지 체크
    :return:
    """
    if 0 <= i < B and 0 <= j < A:
        return True  # 범위 내
    return False  # 범위 벗어님


def crash_robot(robot_name: int):
    """
    다른 로봇과 부딪치는지 체크
    :param i:
    :param j:
    :return:
    """
    for k in range(1, N + 1):  # 로봇들 쯕 보면서
        if k != robot_name:  # 그 로봇이 아닌데
            if robots[robot_name][0] == robots[k][0] and robots[robot_name][1] == robots[k][1]:  # 위치가 같으면
                return k
    return False


def turn_L(robot_name: int, cnt: int):
    """
    왼쪽으로 90도 회전
    :param i:
    :param j:
    :return:
    """
    d = robots[robot_name][2]  # 로봇의 현재 방향
    cnt = cnt % 4
    if d == 'N':
        cnt = cnt % 4

    elif d == 'E':
        cnt = (cnt + 3) % 4

    elif d == 'S':
        cnt = (cnt + 2) % 4
    elif d == 'W':
        cnt = (cnt + 1) % 4
    return l_direction[cnt]


def turn_R(robot_name: int, cnt: int):
    """
    왼쪽으로 90도 회전
    :param i:
    :param j:
    :return:
    """
    d = robots[robot_name][2]  # 로봇의 현재 방향
    cnt = cnt % 4
    if d == 'N':
        cnt = cnt % 4

    elif d == 'E':
        cnt = (cnt + 1) % 4

    elif d == 'S':
        cnt = (cnt + 2) % 4
    elif d == 'W':
        cnt = (cnt + 3) % 4
    return r_direction[cnt]

A, B = map(int, input().split())
N, M = map(int, input().split())
robots = collections.defaultdict(tuple)

for i in range(1, N + 1):  # 로봇 초기 위치, 방향 입력 받기
    x, y, d = input().split()
    robots[i] = [B - int(y), int(x) - 1, d]  # y, x좌표, 방향을 입력받음

# print(robots)
def sol():
    for _ in range(M):  # 명령
        robot_name, command, command_cnt = input().split()
        robot_name = int(robot_name)
        command_cnt = int(command_cnt)
        i, j = robots[robot_name][:2]  # 로봇의 명령 수행 이전 위치

        if command == 'L':
            d = turn_L(robot_name, command_cnt)
            robots[robot_name][2] = d
        elif command == 'R':
            d = turn_R(robot_name, command_cnt)
            robots[robot_name][2] = d

        elif command == 'F':
            i, j = robots[robot_name][:2]  # 로봇 원래 위치
            dire = robots[robot_name][2]  # 로봇 원래 방향

            for k in range(command_cnt):
                i = i + direction_move_index[dire][0]
                j = j + direction_move_index[dire][1]

                robots[robot_name][0] = i
                robots[robot_name][1] = j

                tmp = crash_robot(robot_name)  # 혹시 다른 로봇과 충돌했는지

                if tmp:
                    print('Robot {} crashes into robot {}'.format(robot_name, tmp))
                    return

                if crash_wall(i, j) == False:  # 혹시 범위 넘었는지
                    print('Robot {} crashes into the wall'.format(robot_name))
                    return

        # print(robots)

    else:  # 괜찮으면
        print('OK')


sol()



# print(robots)

"""
5 4
2 2
1 4 E
5 4 W
1 F 3
2 F 1

Robot 2 crashes into robot 1
"""