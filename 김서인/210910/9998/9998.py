# 이분 탐색 - 정중앙의 블록 개수 몇개로 할지
# 동혁이, 윤형이 각각 블록 몇개나 빼거나 쌓아야 할지 (가로 쭉 보면서, 목표 개수 대비해서 빼거나 더하기)
# 오. 왼 해보고 -> 값 작은 쪽으로 가기 (오나 왼을 mid 기준으로 옮기기)
import sys

input = sys.stdin.readline


def cnt_block(center_block):  # 정중앙의 블록 개수를 기준으로 몇 개나 더하고 빼야 할지 개수를 세기
    cnt = 0
    mid_idx = len(yoon_blocks) // 2
    for i in range(mid_idx + 1):  # 절반까지
        cnt += abs(yoon_blocks[i] - (center_block + mid_idx - i))
        cnt += abs(hyuk_blocks[i] - (center_block + mid_idx - i))
    for i in range(mid_idx + 1, len(yoon_blocks)):
        cnt += abs(yoon_blocks[i] - (i - mid_idx + center_block))
        cnt += abs(hyuk_blocks[i] - (i - mid_idx + center_block))
    return cnt


N = int(input())

yoon_blocks = list(map(int, input().split()))
hyuk_blocks = list(map(int, input().split()))
left = 0
right = 10**12 - N//2

# print(left, right)
while left <= right:
    if left == right:
        ans = cnt_block(left)
        break
    mid = (left + right) // 2

    r_cnt = cnt_block(right)
    l_cnt = cnt_block(left)
    # print(left,right)
    if r_cnt > l_cnt:
        # print(1, l_cnt, r_cnt)
        right = mid
    else:
        # print(2, l_cnt, r_cnt)
        left = mid + 1

    # print(left, right, cnt_block((left + right) // 2))

print(ans)