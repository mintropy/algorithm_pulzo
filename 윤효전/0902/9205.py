from pprint import pprint
import collections
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# def find_node(node, pos_list):
#     ret = []
#     for i in range(len(pos_list)):

def bfs(start):
    visit = [0]*(n+2)
    dq = collections.deque()
    dq.append(start)
    while dq:
        tmp = dq.popleft()
        # print(tmp)
        if visit[tmp] == 1:
            continue
        if tmp == n+1:
            return 1

        visit[tmp] = 1
        for v in graph[tmp]:
            dq.append(v)
    return 0


T = int(input())
for _ in range(T):
    n = int(input())
    pos_list = []
    graph = [[] for _ in range(n+2)]
    starty, startx = map(int, input().split())
    pos_list.append((starty, startx))
    for i in range(1, n+1):
        y, x = map(int, input().split())
        pos_list.append((y, x))
    endy, endx = map(int, input().split())
    pos_list.append((endy, endx))

    for i in range(len(pos_list)):
        for j in range(len(pos_list)):
            if i == j:
                continue
            if abs(pos_list[i][0]-pos_list[j][0])+abs(pos_list[i][1]-pos_list[j][1]) <= 1000:
                graph[i].append(j)

    # print(pos_list)
    #print(*graph, sep='\n')
    print(['sad', 'happy'][bfs(0)])
