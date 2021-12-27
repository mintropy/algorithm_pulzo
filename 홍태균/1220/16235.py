'''
나무 재테크

'''
import sys
input = sys.stdin.readline

# 크기, 나무 수, 시간
N, M, K = map(int, input().split())
add_foods = [list(map(int, input().split())) for _ in range(N)]
# 5로 초기화
foods = [[5] * N for _ in range(N)]

# 트리는 빈 리스트로 초기화
# 그리고 추가
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1].append(age)

dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# 연도만큼 반복
for _ in range(K):
    # 봄, 여름
    for i in range(N):
        for j in range(N):
            if trees[i][j] != []:
                # 나무의 어린 순으로 
                trees[i][j].sort()
                # 각 나무본다
                for num in range(len(trees[i][j])):
                    # 각 나무의 나이가 양분보다 적다면 
                    # 가능하기 때문에 양분을 줄이고 나이 증가
                    if foods[i][j] >= trees[i][j][num]:
                        foods[i][j] -= trees[i][j][num]
                        trees[i][j][num] += 1
                    # 그럴 수 없다면 
                    # 각 나무를 양분으로 변화시킨다
                    # 그리고 트리에 그 앞의 나무만 넣는다 그리고 끝
                    else:
                        for tree in trees[i][j][num:]:
                            foods[i][j] += tree//2
                        trees[i][j] = trees[i][j][:num]
                        break
    # 가을 겨울
    for i in range(N):
        for j in range(N):
            if trees[i][j] != []:
                # 각 나무의 나이를 확인
                for tree in trees[i][j]:
                    # 5의 배수이면 번식
                    if tree % 5 == 0:
                        for dir in dirs:
                            nx = i + dir[0]
                            ny = j + dir[1]
                            if 0 <= nx < N and 0 <= ny < N:
                                trees[nx][ny].append(1)
            # 양분 추가
            foods[i][j] += add_foods[i][j]

# 나무 갯수 확인
total = 0
for i in range(N):
    for j in range(N):
        total += len(trees[i][j])

print(total)