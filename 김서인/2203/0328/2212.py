import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

sensors = list(set(sensors)) # 중복 제거
sensors.sort() # 정렬

# 각 수의 간격 구하기 -> 큰 순서대로 없애기 -> 나머지의 합
distances = []
for i in range(len(sensors)-1):
    distances.append(sensors[i+1]-sensors[i])

distances.sort(reverse=True)

print(sum(distances[K-1:]))