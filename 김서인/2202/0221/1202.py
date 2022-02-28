import sys, heapq

input= sys.stdin.readline

N,K = map(int,input().split())
jewelries = []
backpacks = []

for _ in range(N):
    m, v = map(int,input().split())
    jewelries.append((m, v))

for _ in range(K):
    c = int(input())
    backpacks.append(c)

jewelries.sort() # 무게 적은 보석부터 오름차순
backpacks.sort() # 용량 적은 가방부터 오름차순

ans = 0
idx = 0
poss = []
for weight in backpacks: # 가방 용량 적은 것부터 보면서
    # 들어갈 수 있는 보석 있나 보기
    while idx < N:
        m, v = jewelries[idx]
        if m <= weight:
            heapq.heappush(poss, -v) # 가방에 들어갈 수 있는 보석
            idx += 1 # 그 다음 보석
        else: # 못 들어가면 그만두기!!(그 다음 보석도 그것보다 무거워서 가방에 못 넣음)
            break

    if poss:
        ans += -heapq.heappop(poss) # 가방에 넣을 수 있는 보석 중 가격 가장 비싼 것을 넣기

print(ans)