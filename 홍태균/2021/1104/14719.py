'''
빗물

'''
import sys
input = sys.stdin.readline

H, W = map(int,input().split())

blocks = list(map(int,input().split()))

# 맵 만들기
maps = [[0] * W for _ in range(H)]

# 블록 쌓기
for j in range(W):
    for i in range(blocks[j]):
        maps[H-1-i][j] = 1

# 물양
total = 0
# 밑에서부터 확인
for i in range(H-1,-1,-1):
    # 각 줄의 물양
    cnt = 0
    # 줄에 1이 있으면 거기부터 시작
    if 1 in maps[i]:
        idx = maps[i].index(1)
    # 없으면 비어있는 거기 때문에 다음
    else:
        continue

    # 1 다음 1을 찾아서
    for j in range(idx+1,W):
        # 1이면 그동안 0갯수 만큼 더하고 0으로 초기화
        if maps[i][j]:
            total += cnt
            cnt = 0
        # 0이면 물을 추가
        else:
            cnt += 1

print(total)