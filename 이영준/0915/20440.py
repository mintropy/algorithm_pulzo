"""
Title : 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1
Link : https://www.acmicpc.net/problem/20440
"""

# import sys, collections
import sys
input = sys.stdin.readline

n = int(input())
'''
mosquito = collections.defaultdict(lambda: [0, 0])
for _ in range(n):
    enter, exit = map(int, input().split())
    mosquito[enter][0] += 1
    mosquito[exit][1] += 1
'''
mosquito = {}
for _ in range(n):
    enter, exit = map(int, input().split())
    if enter in mosquito:
        mosquito[enter] += 1
    else:
        mosquito[enter] = 1
    if exit in mosquito:
        mosquito[exit] -= 1
    else:
        mosquito[exit] = -1

# 모기가 최대일 때
max_mosquitos: int = 0
# 모기가 최대일 때 시간
max_mosquitos_durations: list = [-1, -1]
# 각 최대 모기수를 처음 만났을 때
is_max_mosquito_fist = True
# 지금 모기 수
mosquitos_now: int = 0

for time in sorted(mosquito.keys()):
    # 지금 시간 이전까지 최대 모기였을 경우
    if mosquitos_now == max_mosquitos and is_max_mosquito_fist:
        mosquitos_now += mosquito[time]
        max_mosquitos_durations[1] = time
        # 모기수가 증가하는 경우
        if mosquitos_now > max_mosquitos:
            is_max_mosquito_fist = True
            max_mosquitos = mosquitos_now
            max_mosquitos_durations = [time, time]
    # 지금 시간 이전까지 최대 모기가 아닌 경우
    else:
        mosquitos_now += mosquito[time]
        is_max_mosquito_fist = False
        # 모기수가 기존 최대 모기수보다 더 많아지는 경우
        if mosquitos_now > max_mosquitos:
            is_max_mosquito_fist = True
            max_mosquitos = mosquitos_now
            max_mosquitos_durations = [time, time]

print(max_mosquitos)
print(*max_mosquitos_durations)


'''
13
2 8
5 6
3 8
1 9
10 56
2 5
6 90
5 8
3 60
4 89
10 13
10 13
10 13

2
0 1100000000
1000000000 2100000000

'''