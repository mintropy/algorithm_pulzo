'''
친구 팰린드롬

'''
import sys
input = sys.stdin.readline

def dfs(n):
    global max_f
    # 마지막 친구까지 왔을 때
    if n == N:
        # 방문을 한 것은 짝을 지은 것이기 때문에 
        # 이것으로 몇명인지 파악
        sum_f = sum(visit)
        # N이 아니라면 1명을 추가
        if sum_f != N:
            sum_f += 1
        if max_f < sum_f:
            max_f = sum_f
        return

    # 방문을 했거나 친구가 없으면 다음 친구로 이동
    if visit[n] or friends[n] == []:
        dfs(n+1)
        return
    # 친구들을 만나면서 짝을 지어준다.
    for next in friends[n]:
        # 이미 짝이 지어져있으면 다음 친구로
        if visit[next]:
            continue
        visit[n] = 1
        visit[next] = 1
        dfs(n+1)
        # 백트래킹
        visit[n] = 0
        visit[next] = 0
    # 다음 친구로
    dfs(n+1)

N, M = map(int,input().split())

# 방문
visit = [0] * (N+1)
# 인접리스트
friends = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int,input().split())
    friends[A].append(B)
    friends[B].append(A)

max_f = 0

dfs(1)
print(max_f)
