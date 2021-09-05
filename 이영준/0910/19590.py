"""
Title : 비드맨
Link : https://www.acmicpc.net/problem/19590
"""

import sys
input = sys.stdin.readline

n = int(input())
beads = [int(input()) for _ in range(n)]

total_beads = sum(beads)
max_bead = max(beads)

if len(beads) == 1:
    print(beads[0])
elif max_bead * 2 > total_beads:
    print(max_bead - (total_beads - max_bead))
else:
    print(total_beads % 2)


'''
# 시간 초과
import sys
input = sys.stdin.readline

n = int(input())
beads = sorted([int(input()) for _ in range(n)])

# 없어지지 않은 시작점
st = 0
# 지금 보고 있는 왼쪽 / 오른쪽
left, right = 0, n - 1

# 지금 보고 있는 외쪽의 구슬 개수
left_count = beads[0]
# 마지막에는 한 종류만 남게 됨
while st < n:
    if left == right:
        break
    # 가장 오른쪽이 1개가 되면, 가능한 모두 제거, 종료
    if right == n - 1 and beads[-1] == 1:
        while True:
            if left + 1 > right:
                break
            beads[left] -= 1
            beads[right] -= 1
            if not beads[left]:
                left += 1
            right -= 1
        break
    # 아닐 때,
    # r_now 기준으로 확인하며 진행
    # 1. 왼쪽이 l_now이면 하나씩 부딪히고 가장 오른쪽으로 이동
    # 2. 
    # 3. 왼쪽과 개수가 같다면 하나 부딪히고 왼쪽으로 이동
    # 4. 왼쪽과 개수의 차이가 둘 이상이면 같아질때까지 부딪히고 가장 오른쪽으로 이동
    else:
        if right - left == 1:
            beads[left] -= 1
            beads[right] -= 1
            right = n - 1
        elif beads[right] == beads[right - 1]:
            if right == n - 1 or beads[right] > beads[right + 1]:
                beads[left] -= 1
                beads[right] -= 1
                right -= 1
            else:
                right = n - 1
        elif beads[right] == beads[right -1] + 1:
            beads[left] -= 1
            beads[right] -= 1
            right -= 1
        else:
            diff = beads[right] - beads[right - 1]
            if diff >= beads[left]:
                beads[right] -= beads[left]
                beads[left] = 0
                left += 1
            else:
                beads[right] -= diff
                beads[left] -= diff
                right = n - 1
    # 왼쪽 구슬이 0개면 하나 오른쪽으로
    if not beads[left]:
        left += 1
        if right == left:
            right = n - 1

print(beads[left])
'''


'''
Counter Example
8
2
2
2
3
3
3
5
6
ans : 0

9
2
2
2
3
3
3
5
5
6
ans : 1

3
5
10
15
ans : 0
'''