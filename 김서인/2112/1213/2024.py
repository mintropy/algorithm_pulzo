import collections
import sys

input = sys.stdin.readline

M = int(input())

# 입력 받기
lines = []
while True:
    start, end = map(int, input().split())
    # 입력 끝
    if start == 0 and end == 0:
        break

    if start == end:  # 출발, 끝점 같으면 필요 X
        continue

    if start < 0 and end <= 0:  # 출발점이 음수이고, 끝나는 점이 0 이하이면 필요 X
        continue

    lines.append((start, end))

sorted_lines = collections.deque(sorted(lines))  # 정렬(출발점 빠른 순 -> 출발점 같으면, 끝나는 점 빠른 순)


def sol():
    finish_idx = 0  # 지금 상황에서 끝나는 점
    use_line_cnt = 0  # 사용한 선의 개수

    while sorted_lines:  # 쯕~ 보자!
        candidates = []  # 지금 쓸 수 있는 후보

        # 일단 하나를 꺼냄
        now_line = sorted_lines.popleft()
        if now_line[0] <= finish_idx:  # 전에 꺼가 끝나는 것보다 일찍 시작하면
            candidates.append(now_line[1])  # 후보에 넣기

        if finish_idx < now_line[0]:  # 가장 빨리 시작하는 선분이 이전 선분이 끝나는 좌표보다 나중에 시작하면
            # 선 덮는 방법 존재하지 않음
            return 0

        # 후보들(지금 선분 끝나는 것보다 일찍 시작하는 점들)
        while sorted_lines:
            tmp = sorted_lines.popleft()

            if tmp[0] <= finish_idx:  # 이전 것이 끝나는 것보다 일찍 시작
                candidates.append(tmp[1])  # 후보에 넣기

            else:  # 아니면
                sorted_lines.appendleft(tmp)
                break  # 이제 후에 나올 아이들은 시작점이 더 나중이니까, 더 이상 후보 나올 수 없으니 break

        finish_idx = max(candidates)  # 끝나는 시점 업데이트 (지금 선분 끝나는 것보다 일찍 시작하는 점들 중에, 젤 늦게 끝나는 것)
        use_line_cnt += 1  # 선분 하나 사용했으니 1 추가

        if finish_idx >= M:  # M까지 왔으면
            return use_line_cnt

    return 0


print(sol())
