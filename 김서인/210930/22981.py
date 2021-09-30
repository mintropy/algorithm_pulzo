import math
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
working_speeds = list(map(int, input().split()))

working_speeds.sort()

fastest = 0
team_a_slowest_person_speed = working_speeds[0]  # a 팀에서 젤 느린 작업 속도는 전체에서 젤 느린 작업 속도

for i in range(1, N):  # 팀 A에 i명 있을 때(i에는 1 ~ N-1이 들어감)
    team_a_working_speed = team_a_slowest_person_speed * i
    team_b_working_speed = working_speeds[i] * (N - i)

    fastest = max(fastest, team_a_working_speed + team_b_working_speed)

if K % fastest:
    print(K//fastest+1)  # 작업 시간을 분 단위로 출력 (일이 끝난 시간이어야 하니까 올림)
else:
    print(K//fastest)