'''
최소 회의실 개수

'''
import sys
input = sys.stdin.readline
import heapq

N = int(input().strip())

confs = []
for _ in range(N):
    # confs.put(tuple(map(int,input().split())))
    heapq.heappush(confs,list(map(int,input().split())))

rooms = []

# 처음 시작을 0을 하였다.
heapq.heappush(rooms, 0)
# 처음 룸을 잡기 때문에 1로 시작
answer = 1
# N개의 회의를 탐색
for i in range(N):
    # heappop을 통해서 start가 낮은 confs를 뽑아낸다.
    conf = heapq.heappop(confs)
    # rooms의 가장 낮은 end와 해당 회의를 start를 비교
    # start가 더 늦으면 그 회의실의 현재 end를 빼낸다.
    if rooms[0] <= conf[0]:
        heapq.heappop(rooms)
    # start가 더 빠르면 새로운 회의실을 사용해야 하기때문에
    # 회의실을 늘린다
    else:
        answer += 1
    # 해당 회의를 end를 넣는다
    heapq.heappush(rooms, conf[1])

print(answer)