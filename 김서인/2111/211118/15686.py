import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, M = MIIS()

city_map = list(list(MIIS()) for _ in range(N))

# 치킨집 위치 찾기
chicken_shop = []
chicken_shop_cnt = 0
for i in range(N):
    for j in range(N):
        if city_map[i][j] == 2:
            chicken_shop.append((i,j))
            chicken_shop_cnt += 1

# 치킨집 중 M개만 뽑기(조합)
def pick(depth, before_idx, history):
    if depth==M:
        remain_chicken_shop.append(tuple(map(int,history.split())))
        return

    for i in range(before_idx, chicken_shop_cnt):
        pick(depth+1, i+1, history + ' '+str(i))


remain_chicken_shop = []
if chicken_shop_cnt > M:
    pick(0,0,'')

else:
    remain_chicken_shop.append(list(range(chicken_shop_cnt)))

ans = 1000000000
# 각각 경우 보면서 도시의 치킨 거리 보기
for i in range(len(remain_chicken_shop)):
    chicken_dist = 0
    # 각 집
    for j in range(N):
        for k in range(N):
            if city_map[j][k]==1: # 집마다 '치킨 거리' 찾기
                chicken_dist_per_house = 100000
                for chicken_house_idx in remain_chicken_shop[i]: # 집에서 어떤 치킨 집이 젤 가깝나
                    chicken_house = chicken_shop[chicken_house_idx]
                    chicken_dist_per_house = min(chicken_dist_per_house, abs(chicken_house[0]-j)+abs(chicken_house[1]-k))


                chicken_dist += chicken_dist_per_house

    ans = min(ans, chicken_dist) # 각 경우(어떤 치킨집 M개 남겨두나)에 따라 도시 치킨 거리 업데이트
# 도시의 치킨 거리 최소-> 정답
print(ans)