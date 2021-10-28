import sys

input = sys.stdin.readline

N = int(input())
origin_lines = list(tuple(map(int, input().split())) for _ in range(N))

origin_lines.sort()  # 정렬

# 맨 처음 꺼 기준으로
start = origin_lines[0][0]
end = origin_lines[0][1]

ans = 0
for k in range(1, N):  # 나머지 선들 보자
    now_start, now_end = origin_lines[k]

    # 겹치는 경우 => 시작점은 무조건 원래 있던 게 더 앞섬. 도착점은 비교해서 정하기.
    if end > now_start:
        end = max(end, now_end)

    # 안 겹치는 경우
    else:
        # 기존 것을 ans에 더하기
        ans += (end - start)
        # 새로운 걸로 업데이트
        start, end = now_start, now_end

ans += (end - start)
print(ans)
