N, C = map(int, input().split())

houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()  # 정렬

left = 1  # 가장 가까운 공유기의 거리가 젤 작으면 1
right = houses[-1]  # 가장 가까운 공유기의 거리가 젤 크다면 마지막 집 위치


def howManyShare(distance):  # distance가 가장 인접한 두 공유기 사이의 거리라면(공유기들은 그 distance 이상으로 떨어져야 함)하면, 몇개나 공유기가 필요한지
    count = 1  # 첫번째 공유기는 첫번째 집에 놓는다
    beforeState = min(houses)
    for i in houses:
        if (i - beforeState) >= distance:  # 공유기가 설치된 집 간의 위치가 distance보다 크거나 같을 때, 두번째 공유기를 둔다.
                                        # (더 작을 때 두면, 가장 인접한 두 공유기 사이 거리가 distance보다 작아짐)
            count += 1
            beforeState = i
    return count # 배치한 공유기 개수


ans = 0
while left <= right:
    mid = (left + right) // 2  # 이게 '가장 가까운 두 공유기의 거리'라고 생각해보기
    if howManyShare(mid) >= C:  # 결과가 공유기 C개이면, 일단 답이 될 수 있다는 것 ! ans을 바꾸기. 더 좋은 답 있을 수 있으니 left바꾸기
        ans = mid
        left = mid + 1
    # elif howManyShare(mid) > C:  # 결과가 공유기 C개보다 많으면, '가장 가까운 공유기의 거리'를 더 크게 해보기
    #     left = mid + 1
    else:  # 결과가 공유기 C개 미만으로 필요한 것이면, '가장 가까운 공유기의 거리'를 줄여보기
        right = mid - 1

print(ans)
