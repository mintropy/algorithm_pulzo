import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

def find_set(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_set(parent[x])
        return parent[x]


def union(x, y):
    parent[find_set(x)] = parent[find_set(y)]


def kruskal():
    global ans
    A = set()
    cnt = 0
    lines.sort(key=lambda x: x[2])  # 가중치에 의해 정렬

    for line in lines:
        if (line[0], line[1]) not in A:
            if find_set(line[0]) != find_set(line[1]):
                A.add((line[0], line[1]))
                ans += line[2]
                union(line[0], line[1])
                cnt += 1
                if cnt == V:
                    return



V, E = map(int, input().split())

lines = [list(map(int, input().split())) for _ in range(E)]

# 그래프 정점마다 자기를 가리키게 함
parent = list(range(V+1))

ans = 0
kruskal()
print(ans)