import sys

input = sys.stdin.readline

N, M, L = map(int, input().split())
if N > 0:
    rest_area = list(map(int, input().split()))
    rest_area.append(0)
    rest_area.append(L)
    rest_area.sort()


# N이 0이면 휴게소 입력 받을 수 없음.


def check_additional_rest_area_cnt(mid):
    """
    휴게소 간격을 최대 mid로 한다고 했을 때, 더 설치해야 하는 휴게소 개수
    """

    # 만약에 현재 휴게소 0개 라면 따로 처리
    if N == 0:
        tmp = L // mid
        if L % mid == 0:
            return (tmp - 1)
        return tmp

    cnt = 0
    before_rest_area_idx = rest_area[0]
    for i in range(1, N + 2):
        tmp = rest_area[i] - before_rest_area_idx
        if tmp > mid:
            add_cnt = (tmp // mid)  # 중간에 더 설치해야 하는 휴게소 개수
            if before_rest_area_idx + (mid * add_cnt) == rest_area[i]:  # 이미 설치된 곳에 또 설치하진 않아도 됨
                add_cnt -= 1
            cnt += add_cnt  # 그만큼 더하기
        before_rest_area_idx = rest_area[i]

    return cnt


left = 0
right = L
mid = (left + right) // 2
ans = 1001

while left <= right:
    mid = (left + right) // 2  # 휴게소가 없는 구간의 최댓값의 최솟값
    if left == 0 and right == 1:  # N이 0일 때를 위해서 특별 처리..
        mid = 1
    if mid <= 0:
        break
    tmp_cnt = check_additional_rest_area_cnt(mid)

    if tmp_cnt > M:  # 휴게소를 계획보다 더 설치해야 하면
        left = mid + 1  # 휴게소가 없는 구간의 최댓값의 최솟값 넓히기

    else:  # 휴게소를 계획만큼 or 휴게소를 계획보다 덜 설치해야 하면
        right = mid - 1  # 휴게소가 없는 구간의 최댓값의 최솟값 줄이기
        ans = min(ans, mid)  # 정답될 수 있음

print(ans)
