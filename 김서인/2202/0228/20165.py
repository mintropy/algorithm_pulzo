import sys, collections, copy

input = sys.stdin.readline

N, M, R = map(int, input().split())
game_map = list(list(map(int, input().split())) for _ in range(N))
origin_height = copy.deepcopy(game_map)

attacker_score = 0

for _ in range(R):  # 라운드
    # 공격수의 행동
    x, y, d = input().split()
    domino = collections.deque()
    x, y = int(x) - 1, int(y) - 1

    domino.append((x, y, game_map[x][y]))
    while domino:
        i, j, height = domino.popleft()

        idx = 0
        while idx < height:

            if d == 'E':
                if j + idx < M:
                    if game_map[i][j + idx] != 0:
                        domino.append((i, j + idx, game_map[i][j + idx]))
                        attacker_score += 1
                        game_map[i][j + idx] = 0
                else:
                    break

            elif d == 'W':
                if 0 <= j - idx:
                    if game_map[i][j - idx] != 0:
                        domino.append((i, j - idx, game_map[i][j - idx]))
                        attacker_score += 1
                        game_map[i][j - idx] = 0
                else:
                    break

            elif d == 'S':
                if i + idx < N:
                    if game_map[i + idx][j] != 0:
                        domino.append((i + idx, j, game_map[i + idx][j]))
                        attacker_score += 1
                        game_map[i + idx][j] = 0
                else:
                    break
            elif d == 'N':
                if 0 <= i - idx:
                    if game_map[i - idx][j] != 0:
                        domino.append((i - idx, j, game_map[i - idx][j]))
                        attacker_score += 1
                        game_map[i - idx][j] = 0


                else:
                    break

            idx += 1

    # 수비수의 행동
    x1, y1 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    game_map[x1][y1] = origin_height[x1][y1]

print(attacker_score)
for i in range(N):
    for j in range(M):
        if game_map[i][j] == 0:
            print('F', end=' ')
        else:
            print('S', end=' ')
    print()
