import sys

def DFS(n):
    # 체크 배열에 기록하여 다시 방문 안하게 함
    chk[n] = 1
    # 결과 배열에 넣음
    res.append(n)
    # 연결된 노드가 있다면
    if n in routes:
        # 그 노드들을 불러와
        next_nodes = routes[n]
        # 순회하며
        for next_node in next_nodes:
            # 다녀간 적 없는 노드라면
            if chk[next_node] == 0:
                # 방문함
                DFS(next_node)

def BFS():
    # 큐가 빌 때까지
    while queue:
        # 큐의 0번 인덱스에서 값을 뽑아
        n = queue.pop(0)
        # 만약 다녀간 노드라면 건너뜀
        # DFS와 달리 큐를 쓰기 때문에 해야함
        if chk[n] == 1:
            continue
        # 아니면 체크
        chk[n] = 1
        # 결과 배열에 넣음
        res.append(n)
        # 이하동일
        if n in routes:
            next_nodes = routes[n]
            for next_node in next_nodes:
                if chk[next_node] == 0:
                    # 큐에 다음 노드를 넣음
                    queue.append(next_node)

N, M, V = map(int, sys.stdin.readline().split())
# 체크 배열과, 결과 배열, 노드별 가능한 경로를 담은 딕셔너리
chk = [0 for _ in range(N + 1)]
res = []
routes = {}
# 입력으로 주어진 경로, 양방향 그래프를 딕셔너리에 넣음
# 배열로 하려다가 N의 크기가 최대 1000이고, 그에 반해 M은 10000밖에 안돼서 딕셔너리 씀
for _ in range(M):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    if node_1 in routes:
        routes[node_1].append(node_2)
        routes[node_1].sort()
    else:
        routes[node_1] = [node_2]
    if node_2 in routes:
        routes[node_2].append(node_1)
        routes[node_2].sort()
    else:
        routes[node_2] = [node_1]

DFS(V)
print(' '.join(map(str, res)))

chk = [0 for _ in range(N + 1)]
res = []
queue = [V]
BFS()
print(' '.join(map(str, res)))