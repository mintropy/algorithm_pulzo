'''
내일 할거야

'''
import sys
input = sys.stdin.readline

N = int(input())

# homeworks = [list(map(int,input().split())) for _ in range(N)]

# homeworks.sort(key=lambda x:-x[1])
# 숙제의 마감 날짜의 내림차순으로 정렬
homeworks = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:-x[1])

# 시작 날짜는 마감 날짜가 가장 큰 것부터
idx = homeworks[0][1]
for d, t in homeworks:
    # 현재 날짜와 해당 숙제의 마감 날짜 중 작은 값
    idx = min(idx,t)
    # 숙제의 수행 기간 만큼 줄인다.
    idx -= d

print(idx)
