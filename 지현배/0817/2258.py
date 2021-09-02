import sys
input = sys.stdin.readline
def sol():
    N, M = map(int, input().split())
    steak = [list(map(int, input().split())) for _ in range(N)]
    # 가격에 대해 오름차순, 무게에 대해 내림차순 정렬
    steak.sort(key=lambda x: (x[1], -x[0]))
    # 모든 고기 무게의 합
    total = 0
    for i in range(N):
        total += steak[i][0]
    # 합이 목적 무게보다 적다면 -1
    if total < M:
        return -1
    # 첫 비교 가격은 가장 비싼 고기의 가격
    cost = steak[-1][1]
    # 스택에 넣는다
    stack = [cost]
    # 가장 비싼 고기 제외하고 순회
    for i in range(N - 2, -1, -1):
        # 총 무게에서 전 시퀀스의 고기의 무게를 뺀다
        total -= steak[i + 1][0]
        # 그 무게가 여전히 목적 무게보다 같거나 크다면
        if total >= M:
            # 지금의 가격을 비교 가격에 넣는다
            cost = steak[i][1]
            # 이 가격이 가장 최근에 스택에 넣은 무게랑 같지 않다면
            if cost != stack[-1]:
                # 스택에 넣는다
                stack.append(cost)
        # 지금의 무게가 목적 무게보다 작다면
        # 최소 전 시퀀스의 고기를 포함해야 목적 무게를 달성할 수 있다
        else:
            # 지금 포함되어있는 고기 중 전 시퀀스의 고기의 가격과 같은 고기가 몇 개가 있는지 센다
            # 타겟 인덱스는 전 고기부터 시작한다
            idx = i + 1
            # 자신을 포함하여 일단 한 개가 있다
            cnt = 1
            # 타겟인덱스가 0보다 작아지면 그만 센다
            while idx >= 0:
                # 자기 자신을 위에서 포함했으므로 패스한다
                if idx == i: 
                    idx -= 1
                    continue
                # 두 고기의 가격이 같다면
                if steak[i][1] == steak[idx][1]:
                    # 카운트를 늘리고 인덱스를 줄인다
                    cnt += 1
                    idx -= 1
                # 다르면 그만 센다
                else:
                    break
            # 스택의 길이가 1보다 크고(가장 비싼 고기가 아닐 때) 이것보다 비싼 고기보다 가성비가 떨어지면
            if len(stack) > 1 and stack[-2] < cnt * cost:
                # 그것보다 한단계 비싼 고기를 선택한다
                return stack[-2]
            # 아니라면 그 고기를 산다
            else:
                return cnt * cost
    # 고기가 한덩어리밖에 없을때
    else:
        return cost
print(sol())


'''
11 60
8 0
8 1
5 1
1 1
10 2
3 2
2 2
20 3
18 3
10 3
30 8
'''