#  가장 가까운 조상 노드 찾기
def find_shortest():
    for i in range(len(a_list)):
        a_tmp = a_list[i]
        for j in range(len(b_list)):
            b_tmp = b_list[j]
            if a_tmp == b_tmp:
                print(a_tmp)
                return

T = int(input())

for _ in range(T):
    N = int(input())
    adj = [[0] * 2 for _ in range(N+1)] # 부모 노드, 자식 노드들
    for _ in range(N - 1):
        parent, child = map(int, input().split())
        adj[child][0] = parent
        if adj[parent][1]: # 자식 있으면
            adj[parent][1].append(child)
        else:
            adj[parent][1] = [child]

    a, b= map(int,input().split())
    a_list = []
    b_list = []
    while True:
        a_list.append(a)
        b_list.append(b)
        a = adj[a][0]
        b = adj[b][0]
        if a==0 and b==0:
            break

    find_shortest()
