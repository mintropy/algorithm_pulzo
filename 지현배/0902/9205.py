import sys
input = sys.stdin.readline
def sol(curr):
    # 페스티벌 갈 수 있으면 'happy'
    if abs(curr[0] - fstv[0]) + abs(curr[1] - fstv[1]) <= 1000:
        global res
        res = 'happy'
        return
    # 모든 노드에 대하여 (1) 간 적 없고, (2) 갈 수 있다면 진입
    for i in range(N):
        if check[i] == False and abs(curr[0] - conv[i][0]) + abs(curr[1] - conv[i][1]) <= 1000:
            check[i] = True
            sol(conv[i])
            # 이미 확인한 노드는 다시 갈 필요가 없으므로 visit 해제하지 않음
            # check[i] = False 

T = int(input())
for _ in range(T):
    N = int(input())
    home = tuple(map(int, input().split()))
    conv = [[] for _ in range(N)]
    check = [False for _ in range(N)]
    res = 'sad'
    for n in range(N):
        conv[n] = tuple(map(int, input().split()))
    fstv = tuple(map(int, input().split()))
    sol(home)
    print(res)
    