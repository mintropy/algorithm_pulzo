N = int(input())
arr = input()
balls = []

target_ball = arr[0]
cnt = 1
idx = 1

while idx <= N:
    if idx == N:
        balls.append((target_ball, cnt))
        break

    if target_ball == arr[idx]:
        cnt += 1
    else:
        balls.append((target_ball, cnt))
        cnt = 1
        target_ball = arr[idx]

    idx += 1

# 빨간 공을 왼쪽으로 모우기 => (맨 왼쪽 빨강들을 제외한 빨강들 만큼 움직이기)
idx = 1  # 맨 왼쪽이 빨강이든 파랑이든 안 세도 됨.
red_left = 0
while idx < len(balls):
    if balls[idx][0] == 'R':
        red_left += balls[idx][1]
    idx += 1

# 파랑 공을 왼쪽으로 모우기 => (맨 왼쪽 파랑 빼고 나머지 파랑 만큼 움직이기)
idx = 1  # 맨 왼쪽이 빨강이든 파랑이든 안 세도 됨.
blue_left = 0
while idx < len(balls):
    if balls[idx][0] == 'B':
        blue_left += balls[idx][1]
    idx += 1

# 파랑 공을 오른쪽으로 모우기 => (맨 오른쪽 파랑 빼고 나머지 파랑 만큼 움직이기)
idx = len(balls) - 2  # 맨 오른쪽이 빨강이든 파랑이든 안 세도 됨.
blue_right = 0
while idx >= 0:
    if balls[idx][0] == 'B':
        blue_right += balls[idx][1]
    idx -= 1

# 빨강 공을 오른쪽으로 모우기 => (맨 오른쪽 빨강 빼고 나머지 빨강 만큼 움직이기)
idx = len(balls) - 2  # 맨 오른쪽이 빨강이든 파랑이든 안 세도 됨.
red_right = 0
while idx >= 0:
    if balls[idx][0] == 'R':
        red_right += balls[idx][1]
    idx -= 1

print(min(blue_left, red_left, blue_right, red_right))
