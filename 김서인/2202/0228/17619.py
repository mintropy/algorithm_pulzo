import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

line = [[*map(int, input().split())] + [i] for i in range(1, N + 1)]  # 원래 인덱스를 저장해야 하므로!!
line.sort(key=lambda x: (x[0], -x[1]))

connect = [0] * (N + 1)

right = line[0][1]
idx = 0
for i in range(1, N):
    a, b = line[i][0], line[i][1]
    if right < a:  # 안 겹칠 때
        right = b
        idx += 1
        connect[line[i][3]] = idx

    elif right < b:  # 겹칠 때
        right = b
        connect[line[i][3]] = idx  # 원래 인덱스 위치에 저장
    elif b <= right:  # 겹칠 때
        connect[line[i][3]] = idx  # 원래 인덱스 위치에 저장

for _ in range(Q):
    x1, x2 = map(int, input().split())
    if connect[x1] == connect[x2]:
        print(1)
    else:
        print(0)
