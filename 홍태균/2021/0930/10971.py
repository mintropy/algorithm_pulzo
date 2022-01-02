'''
외판원 순회 2

'''
import sys
input = sys.stdin.readline

N = int(input())

W = [list(map(int,input().split())) for _ in range(N)]
# 방문
visit = [0] * N

# DFS/ 위치, 비용, 처음위치, 이동 횟수
def dfs(d,w,st_d,cnt):
    # 최소 횟수
    global min_w

    # 모든 마을을 방문했을 때
    if cnt == N:
        # 마지막 방문한 마을에서 처음 마을로 갈 수 있는 지
        if W[d][st_d]:
            if min_w > w + W[d][st_d]:
                min_w = w + W[d][st_d]
        else:
            return
    
    # 방문
    visit[d] = 1
    # 인접 마을 순회
    for i in range(N):
        # 인접 마을이 연결되어 있고 방문 안했으면
        if W[d][i] > 0 and visit[i] == 0:
            # 인접 마을 이동, 비용 증가, 처음 위치, 횟수 증가
            dfs(i,w + W[d][i],st_d,cnt + 1)
            # 다시 방문 해제
            visit[i] = 0
# 최소
min_w = 1000000 * (N + 2)

# 모든 마을에서 시작
for i in range(N):
    dfs(i,0,i,1)

print(min_w)


'''
2
1000000 1000000
1000000 1000000
'''