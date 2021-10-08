import sys

input = sys.stdin.readline

N, M = map(int, input().split())
friends = list([] for _ in range(N + 1))

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

ans = 0
visited = [False] * (N + 1)


def dfs(curr, cnt):
    global ans

    if ans < cnt:
        ans = cnt

    if curr == N:
        return

    if visited[curr] == False:  # 아직 짝이 안 지어졌으면, 친구 찾는 경우를 고려하기 (짝을 지어보기)
        for i in range(curr + 1, N + 1):
            if visited[i] == False and i in friends[curr]:  # 방문 안 했고 친구이면
                visited[i] = True
                visited[curr] = True
                dfs(curr+1, cnt + 2)  # 그 쌍을 더함
                visited[i] = False
                visited[curr] = False

    # 친구 안 찾는 경우를 고려하기 (짝 안 지어보기)
    dfs(curr + 1, cnt)


for i in range(1, N + 1):  # 1번부터 쭉 보면서!
    dfs(i, 0)

if N > ans:  # 전체 학생 중에 배치 안한 사람이 있으면, 혼자 로봇 춤 추는 경우 추가
    print(ans + 1)
else:
    print(ans)
