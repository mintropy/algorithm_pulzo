import sys
input = sys.stdin.readline
N, M = map(int, input().split())
space = [input().rstrip() for _ in range(N)]
PR, PC = map(lambda x: int(x) - 1, input().split())
nc = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
direction = ['U', 'R', 'D', 'L']
# 최소 위쪽 방향 1초
res = ['U', 1]
for i in range(4):
    d = direction[i]
    y, x = PR, PC
    # 시작점 포함 1초
    cnt = 1
    while True:
        y, x = y + nc[d][0], x + nc[d][1]
        # 종료조건 1. 시작할때와 같은 방향으로 시작점으로 들어오면 'Voyager'
        if y == PR and x == PC and d == direction[i]:
            # 'Voyager'가 여러개 나올때 덮어씌워지는 것을 방지
            if res[1] != 'Voyager':
                res = [direction[i], 'Voyager']
            break
        # 종료조건 2. 범위를 벗어나거나 블랙홀에 빠졌을 때
        if not 0 <= y < N or not 0 <= x < M or space[y][x] == 'C':
            # 'Voyager'가 아니거나 카운트가 더 많으면 덮어씌움
            if res[1] != 'Voyager' and res[1] < cnt:
                res = [direction[i], cnt]
            break
        # 방향에 따라 방향 스왑
        elif space[y][x] == '/':
            if d == 'U': d = 'R'
            elif d == 'R': d = 'U'
            elif d == 'D': d = 'L'
            else: d = 'D'
        elif space[y][x] == '\\':
            if d == 'U': d = 'L'
            elif d == 'L': d = 'U'
            elif d == 'D': d = 'R'
            else: d = 'D'
        # 카운팅
        cnt += 1
print(*res, sep='\n')