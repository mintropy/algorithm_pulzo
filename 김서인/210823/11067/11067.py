import sys

input = sys.stdin.readline

# 항상 서쪽 -> 동쪽으로만 간다! 반대로 안감. (X 축 늘어나는 방향으로만 가야 함)
# 같은 X축에 여러 개의 카페가 있을 수도 있는데, 모두 방문해야 함! (X 같은 것이 여러 개라면, 이전 것과 y축 차이가 적은 것부터 가기)

T = int(input())
for _ in range(T):
    N = int(input())
    cafes = list(tuple(map(int, input().split())) for _ in range(N))
    # 정렬: X축 낮은 순서대로
    cafes.sort()

    # print(cafes)

    final_cafes = [(-1, 0)]
    cur_x, cur_y = (-1, 0)
    same_y = [(-1, 0)]  # 같은 X축에 다른 Y축인 카페가 여러 개라면 리스트에 저장
    i = 0
    while i < N:
        if cur_x == cafes[i][0]:
            same_y.append(cafes[i])

        else:
            # X축이 같은 카페를 배치하기
            if final_cafes[-1][1] != same_y[0][1]:  # 만약 순서가 맞지 않으면 거꾸로 해주기
                same_y.reverse()
            final_cafes.extend(same_y)
            same_y = [cafes[i]]
            cur_x, cur_y = cafes[i]
        i += 1

    # 마지막 부분을 final_cafes에 안 넣었으면
    if same_y[0] not in final_cafes:
        if final_cafes[-1][1] != same_y[0][1]:  # 만약 순서가 맞지 않으면 거꾸로 해주기
            same_y.sort(reverse=True)
        final_cafes.extend(same_y)

    print(final_cafes)

    # 출력할 카페 번호 받아오기 
    where_cafes = list(map(int, input().split()))

    # 각각 카페 위치 출력하기 (맨 처음 꺼는 몇 개인지 하는 거라서 빼고!)
    for i in range(1, len(where_cafes)):
        print(*final_cafes[where_cafes[i]+1])
