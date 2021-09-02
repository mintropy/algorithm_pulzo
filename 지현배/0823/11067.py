import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    cafe = [tuple(map(int, input().split())) for _ in range(N)]
    M, *numbers = map(int, input().split())
    cafe.sort(key=(lambda x: (x[0], x[1])))
    print(cafe)
    # 카페 좌표를 번호 순으로 나열
    ca_num = [(-1, 0)]
    n = 1
    # 이전 좌표
    x, y = -1, 0
    answer = []
    # 탐색위한 인덱스 변수
    idx = 0
    while idx < len(cafe):
        # 현재 x 좌표와 같은 좌표를 구한다.
        cnt = 1
        while idx + cnt < len(cafe):
            if cafe[idx + cnt][0] == cafe[idx][0]:
                cnt += 1
            else: break
        # 방향성에 따라 넘버링을 한다.
        i = 0
        if y == cafe[idx][1]:
            while i < cnt:
                ca_num.append(cafe[idx + i])
                i += 1
            x, y = cafe[idx + cnt - 1]
        elif y == cafe[idx + cnt - 1][1]:
            while i < cnt:
                ca_num.append(cafe[idx + cnt - 1 - i])
                i += 1
            x, y = cafe[idx]
        idx += cnt
    for n in numbers:
        print(*ca_num[n])
