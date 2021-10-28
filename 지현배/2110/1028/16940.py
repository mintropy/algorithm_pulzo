import sys
input = sys.stdin.readline
def sol():
    N = int(input())
    edges = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)
    arr = tuple(map(int, input().split()))
    visited = [True] * (N + 1)
    visited[1] = False
    idx = 1
    for i in arr:
        # 방문체크가 안된 노드가 있으면 잘못된 BFS
        if visited[i]:
            return 0
        # 현재 노드에서 방문할 수 있는 노드들을 next_list에 넣는다.
        next_list = []
        for e in edges[i]:
            if visited[e]:
                visited[e] = False
                next_list.append(e)
        # idx부터 next_list의 길이만큼 탐색하며 올바른 BFS인지 확인한다.
        next_list.sort()
        new_arr = sorted(arr[idx:idx + len(next_list)])
        for i in range(len(next_list)):
            if new_arr[i] == next_list[i]:
                visited[new_arr[i]] = False
            else:
                return 0
        idx += len(next_list)
        if idx >= N:
            return 1
    else:
        return 1
print(sol())