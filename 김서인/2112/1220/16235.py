import sys

input = sys.stdin.readline
MIISS = lambda: map(int, input().strip().split())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

N, M, K = MIISS()
nutriment_volume = [list(MIISS()) for _ in range(N)]  # 겨울에 주는 양분의 양

ground_nutriment = [[5] * N for _ in range(N)]  # 현재 밭 양분
ground_tree = [[[] for _ in range(N)] for _ in range(N)]  # 현재 나무 현황
for _ in range(M):
    x, y, z = MIISS()
    ground_tree[x - 1][y - 1].append(z)

for _ in range(K):  # K년 반복
    # 봄
    for i in range(N):
        for j in range(N):  # 그 땅에
            dead_trees_start_idx = -1
            tmp = ground_tree[i][j]
            if tmp:  # 나무 있으면
                tmp.sort()  # 나이 적은 나무부터
                for k in range(len(tmp)):  # 여러 나무일 수도 있음
                    if ground_nutriment[i][j] - tmp[k] >= 0:  # 해당 나무가 자기 나이만큼 양분 먹을 수 있으면
                        ground_nutriment[i][j] -= tmp[k]
                        tmp[k] += 1  # 나무 나이 1 증가
                    else:  # 못 먹으면 죽는다.
                        # 이제 나이 더 많은 나무만 남음 -> 그 나무들도 죽은 나무에 넣고 break
                        dead_trees_start_idx = k
                        break
                # 죽은 나무들 빼기
                if dead_trees_start_idx != -1:
                    ground_tree[i][j] = ground_tree[i][j][:dead_trees_start_idx]
                    for k in range(dead_trees_start_idx, len(tmp)):
                        # 여름 - 죽은 나무마다 나이를 2로 나눈 값(소수점 버리기)이 그 칸에 양분으로 추가
                        ground_nutriment[i][j] += (tmp[k] // 2)

    # 가을
    new_trees = []
    for i in range(N):
        for j in range(N):  # 그 당에
            for tree in ground_tree[i][j]:  # 나무 하나씩 보면서
                if tree % 5 == 0:  # 나이가 5의 배수이면 번식한다.
                    for ki, kj in directions:  # 인접한 8개 칸
                        ni, nj = i + ki, j + kj
                        if 0 <= ni < N and 0 <= nj < N:  # 범위 체크
                            ground_tree[ni][nj].append(1)  # 나이가 1인 나무 생긴다.

    # 겨울
    for i in range(N):
        for j in range(N):
            ground_nutriment[i][j] += nutriment_volume[i][j]  # 땅에 양분 추가

# K년 후 남은 나무 개수 세기
alive_trees_cnt = 0
for i in range(N):
    for j in range(N):
        alive_trees_cnt += len(ground_tree[i][j])


print(alive_trees_cnt)

# alive_trees_cnt = 0
# for i in range(N):
#     for j in range(N):
#         if ground_tree[i][j]:
#             for tree in ground_tree[i][j]:
#                 alive_trees_cnt += 1