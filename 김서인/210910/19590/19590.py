# 다른 종류 부딪히면 깨진다. 최대한 구슬을 없애야 함 => 남는 구슬 몇개일까?
# 우선 순위 큐에 넣고, 맨 위에 있는 것 두 종류 부수기! => 시간 초과ㅠ

N = int(input())
beads = list(int(input()) for _ in range(N))
biggest = max(beads)
left = sum(beads) - biggest

if biggest >= left:
    ans = biggest - left

else:
    if sum(beads) % 2:  # 홀수이면
        ans = 1
    else:  # 짝수이면
        ans = 0
print(ans)
