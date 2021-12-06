'''
역사

'''
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
# 맵 만들기
maps = [[0] * (n+1) for _ in range(n+1)]
# 해당 구간들 이어주기
for _ in range(k):
    a, b = map(int,input().split())
    maps[a][b] = 1

s = int(input().strip())
# 플로이드 와샬 알고리즘 적용
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            # 원래 갈수 있거나 해당 구간을 거쳐서 갈 수 있다면 이어주기
            if maps[i][j] == 1 or maps[i][k] + maps[k][j] == 2:
                maps[i][j] = 1

# 해당 구간들이 이어져있는지 확인
for _ in range(s):
    a, b = map(int,input().split())
    # 정방향으로 이어진 구간
    if maps[a][b] == 1:
        print(-1)
    # 역방향으로 이어진 구간
    elif maps[b][a] == 1:
        print(1)
    # 이어지지 않은 구간
    else:
        print(0)
