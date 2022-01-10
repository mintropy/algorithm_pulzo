import sys, copy

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())
# 가로로 봤을 때 상대적인 순서가 같으면 된다.

N, M = MIIS()
arr = list(tuple(MIIS()) for _ in range(N))


# 가로줄의 값들이 n 간격으로 있어야 함.
def check():
    copy_arr = copy.deepcopy(arr)
    copy_arr.sort()

    for i in range(N):
        for j in range(M):
            if i * M + 1 <= copy_arr[i][j] <= (i+1) * M:
                pass
            else:
                return False
    return True

def sol():
    # 맨 처음 줄의 순서
    first_line_order = [0] * M

    first_line = arr[0]
    sorted_first_line = sorted(first_line)

    for i in range(M):
        first_line_order[i] = sorted_first_line.index(first_line[i])

    # 다른 줄
    for i in range(1, N):
        order = [0] * M

        line = arr[i]
        sorted_line = sorted(line)

        for j in range(M):
            order[j] = sorted_line.index(line[j])

        # 비교
        for j in range(M):
            if order[j] != first_line_order[j]:
                return 0

    return 1


if N == 1 or M == 1:  # 한 줄인 경우, 열/행 계속 바꿔서 오름차 순으로 바꿀 수 있음.
    print(1)  # 무조건 정답 가능

else:

    if check() == False:
        print(0)
    else:

        print(sol())


'''
3 3
1 2 3
6 7 8
4 5 9
'''