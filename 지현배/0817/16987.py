import sys
input = sys.stdin.readline
def sol():
    N = int(input())
    eggs = [list(map(int, input().split())) for _ in range(N)]
    crashed = [False for _ in range(N)]
    max_cnt = 0
    def DFS(i, cnt):
        # 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 종료한다.
        if i > N - 1:
            nonlocal max_cnt
            max_cnt = max(max_cnt, cnt)
            return
        # 이미 다 깰 수 있는 경우의 수가 있따면 종료한다.
        if max_cnt == N: return
        # 남은 계란수의 2배와 지금까지 깬 수의 합이 최댓값보다 작으면 종료한다.
        if (N - i) * 2 + cnt < max_cnt:
            return
        # 들고 있는 계란이 깨졌거나 깨지지않은 다른 계란이 없으면 넘어간다.
        if crashed[i] == True or crashed.count(False) == 1:
            DFS(i + 1, cnt)
        else:
            for j in range(N):
                if i == j: continue
                if crashed[j] == False:
                    temp = 0
                    # 부딪혀 보고
                    eggs[i][0] -= eggs[j][1]
                    eggs[j][0] -= eggs[i][1]
                    # 깨지면 깨졌다고 한다
                    if eggs[i][0] <= 0: temp += 1; crashed[i] = True
                    if eggs[j][0] <= 0: temp += 1; crashed[j] = True
                    DFS(i + 1, cnt + temp)
                    # 다음을 위해 복구한다
                    if eggs[i][0] <= 0: crashed[i] = False
                    if eggs[j][0] <= 0: crashed[j] = False
                    eggs[i][0] += eggs[j][1]
                    eggs[j][0] += eggs[i][1]
    DFS(0, 0)
    return max_cnt
print(sol())