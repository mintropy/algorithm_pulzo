"""
Title : 샤워실 바닥 깔기 (Small)
Link  : https://www.acmicpc.net/problem/14600
"""

def rotate_base(base):
    base = list(zip(*base))[::-1]
    return [list(line) for line in base]


k = int(input())
y, x = map(int, input().split())
x = 2 ** k + 1 - x

if k == 1:
    base = [[1, 1], [1, 1]]
    base[x - 1][y - 1] = -1
    for line in base:
        print(*line)
else:
    base = [
        [1, 1, 2, 2],
        [1, 3, 3, 2],
        [4, 3, 5, 5],
        [4, 4, 5, 5]
    ]

    # x, y위치에 딸 회전
    if x <= 2 and y <= 2:
        rotate = 2
    elif x <= 2 and y > 2:
        rotate = 1
    elif x > 2 and y > 2:
        rotate = 0
    else:
        rotate = 3

    for _ in range(rotate):
        base = rotate_base(base)

    base[x - 1][y - 1] = -1

    for line in base:
        print(*line)
