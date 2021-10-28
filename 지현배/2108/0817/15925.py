import sys
input = sys.stdin.readline
def sol():
    N, target = map(int, input().split())
    com = [list(map(int, input().split())) for _ in range(N)]
    # 모두 변했는지 확인하기 위한 변수
    dst = N * N
    total = 0
    # 일단 켜져있는 컴퓨터를 모두 셈
    for i in range(N):
        total += sum(com[i])
    # 모두 끌거라면 1개수에서 0개수로 바꿈
    if target == 0:
        total = dst - total
    # 바뀐게 있는지 없는지 비교하여 확인
    prev_total = total
    while total != dst:
        # 가로줄 확인
        for i in range(N):
            cnt = com[i].count(target)
            if cnt > N // 2:
                com[i] = [target for _ in range(N)]
                total += N - cnt
        # 세로줄 확인
        for j in range(N):
            cnt = 0
            for i in range(N):
                if com[i][j] == target:
                    cnt += 1
            if cnt > N // 2:
                total += N - cnt
                for i in range(N):
                    com[i][j] = target
        # 바뀐게 없으면 0 리턴
        if prev_total == total:
            return 0
        prev_total = total
    # 무사히 끝나면 1 리턴
    else:
        return 1
print(sol())
