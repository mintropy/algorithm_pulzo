from sys import stdin
from collections import deque

'''
n, l, r = map(int, stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))
'''

'''
# case 1 통과
n, l, r = 2, 20, 50
graph = [[50,30],[20,40]]
'''

'''
# case 2 통과
n, l, r = 3, 5, 10
graph = [[10, 15, 20],[20, 30, 25], [40, 22, 10]]
'''

# case 3
n, l, r = 4, 10, 50
graph = [[10,100,20,90],[80,100,60,70],[70,20,30,40],[50,20,100,10]]



# 국경 공유 & 인구 공유
# 국경 공유한 국가 사이 조건 만족하면 진행
def population_move(graph, i, j):
    global visited, n, l, r
    queue = deque([(i, j)])
    visited[i][j] = True
    territory = [(i, j)]
    population = [graph[i][j]]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        # 기준이 되는 국가 위치 x, y, 인구 pop
        x, y = queue.popleft()
        pop = graph[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 국경 인접 국가 존재하고, 확인하지 않았을 때
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    # 인접국 인구 p, 기준 국가와 인구수 차이 확인
                    p = graph[nx][ny]
                    if l <= abs(pop - p) <= r:
                        territory.append((nx, ny))
                        population.append(p)
                        visited[nx][ny] = True
                        queue.append((nx, ny))
    if len(population) == 1:
        return False, graph
    else:
        avg_pop = sum(population) // len(population)
        for i, j in territory:
            graph[i][j] = avg_pop
        return True, graph

count = 0
while True:
    visited = [[False] * n for _ in range(n)]
    da, db = [-1, 1, 0, 0], [0, 0, -1, 1]
    changed = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # 인구 이동을 한 경우 tf를 True로 받음
                # 주변에 한 칸이라도 탐색 가능할때만 bfs 실행
                possible = False
                for k in range(4):
                    na, nb = i + da[k], j + db[k]
                    if 0 <= na < n and 0 <= nb < n:
                        if l <= abs(graph[i][j] - graph[na][nb]) <= r:
                            possible = True
                            break
                if possible:
                    tf, graph = population_move(graph, i, j)
                else:
                    continue
                # 인구 이동이 한 번 이라도 잇었으면 changed 변화
                if tf:
                    changed = True
    # 인구 이동이 있었으면 count더하고, 아니면 출력 후 종료
    if changed:
        count += 1
    else:
        print(count)
        break
