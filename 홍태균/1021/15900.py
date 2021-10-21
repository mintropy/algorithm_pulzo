'''
나무 탈출

'''
import sys
input = sys.stdin.readline

# 깊이 계산
def dfs(n):
    # 스택, 총 깊이 합, 방문
    stack = [(n,0)]
    total = 0
    visit[n] = 1

    while stack:
        node,cnt = stack.pop()
        ck = True
        # 연결되어있는 노드 탐색
        for next in tree[node]:
            # 방문 안한 것을 탐색
            if visit[next] == 0:
                visit[next] = 1
                # 깊이를 더해준다.
                stack.append((next,cnt + 1))
                # 방문할 수 있다는 것을 확인
                ck = False
        # 방문할 노드가 없다는 것은 리프 노드
        # 리프 노드의 깊이를 더해준다.
        if ck:
            total += cnt
    # 총 깊이의 합을 리턴
    return total
            

N = int(input())

tree = [[] for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

ans = dfs(1)
# 깊이의 합이 짝수이면 진다
# 홀수이면 이긴다.
if ans % 2:
    print("Yes")
else:
    print("No")