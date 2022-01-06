'''
골목 대장 호석 - 기능성

'''
import sys
input = sys.stdin.readline

N, M, A, B, C = map(int,input().split())

# 골목과 방문 리스트
roads = [[] for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(M):
    a, b, c = map(int,input().split())
    roads[a].append((b,c))
    roads[b].append((a,c))

# 답을 10000으로 설정 최대가 1000이기 때문에
ans = 10000

# 백트래킹
# 현재 위치, 요금 합, 현재 최대값
def dfs(n,total,max_c):
    global A, B, C, ans
    # B에 도착하면 
    # 최소값인지 확인
    if n == B:
        if ans > max_c:
            ans = max_c
        return

    # 연결된 골목 확인
    for next in roads[n]:
        # 방문 안했고 C 보다 작으면 탐색
        if visit[next[0]] == 0 and total + next[1] <= C:
            visit[next[0]] = 1
            # 최대값 저장
            if max_c < next[1]:
                dfs(next[0],total + next[1],next[1])
            else:
                dfs(next[0],total + next[1],max_c)
            visit[next[0]] = 0
# A는 처음 방문
visit[A] = 1
dfs(A,0,0)

# 답이 그대로 10000일 경우 B에 도착하지 못한 거
if ans == 10000:
    ans = -1
print(ans)