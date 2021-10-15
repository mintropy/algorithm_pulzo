from sys import stdin

'''
# 보드 크기
n = int(stdin.readline().strip())
# 사과 개수
k = int(stdin.readline().strip())
# 사과 위치
apple = []
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    apple.append((a, b))
# 뱀 방향 변환 횟수
l = int(stdin.readline().strip())
# 뱅 방향 변환 정보
turn = []
for i in range(l):
    x, c = map(str, stdin.readline().split())
    turn.append((int(x), c))
'''

'''
# case 1 통과
n = 6
k = 3
apple = [(3, 4), (2, 5), (5, 3)]
l = 3
turn = [(3, 'D'), (15, 'L'), (17, 'D')]
'''
'''
# case 2 통과
n = 10
k = 4
apple = [(1, 2), (1, 3), (1, 4), (1, 5)]
l = 4
turn = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
'''

# case 3
n = 10
k = 5
apple = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
l = 4
turn = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]


def move(x, d):
    global sec, snake, apple
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for i in range(1, x + 1):
        # 머리가 다음 향하는 칸
        h1, h2 = snake[-1][0] + dx[d], snake[-1][1] + dy[d]
        # 머리가 범위를 벗어나면 중단
        if h1 <= 0 or h1 > n:
            return i, False
        elif h2 <= 0 or h2 > n:
            return i, False
        # 머리가 다음 향하는 칸이 이미 있으면 중단
        elif [h1, h2] in snake:
            return i, False
        # 머리가 사과를 먹으면 머리만 추가
        elif (h1, h2) in apple:
            apple.remove((h1, h2))
            snake.append([h1, h2])
            continue
        # 모든 경우가 아니라면 한칸씩 전진
        for j in range(len(snake)):
            if j == len(snake) - 1:
                snake[j] = [h1, h2]
                continue
            snake[j] = snake[j + 1]
    return x, True


# 전체 걸리는 시간
sec = 0
# 뱀의 위치, 꼬리부터 머리까지
snake = [[1, 1]]
# 방향
d = 1
for i in range(l + 1):
    # 회전 사이 시간 조정
    if i == 0:
        x, c = turn[0]
    # 모든 회전을 하고, 진행 가능한 경우
    elif i == l:
        x, c = 100, 'D'
    else:
        x = turn[i][0] - turn[i - 1][0]
        c = turn[i][1]
    # 해당 이동이 걸리는 시간, 모두 이동 가능한지
    # 중간에 멈추는 경우 tf = False로, 중단
    time, tf = move(x, d)
    sec += time
    # 방향 전환
    if c == 'D':
        if d == 3:
            d = 0
        else:
            d += 1
    elif c == 'L':
        if d == 0:
            d = 3
        else:
            d -= 1
    if tf:
        continue
    else:
        print(sec)
        break