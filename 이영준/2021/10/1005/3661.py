"""
Title : 생일 선물
Link : https://www.acmicpc.net/problem/3661
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


for _ in range(int(input())):
    price, n = MIIS()
    able = list(MIIS())
    
    # 모든 사람 가능 금액이 선물 금액 넘는 경우
    if sum(able) < price:
        print('IMPOSSIBLE')
        continue
    # 정확히 금액이 일치하는 경우
    elif sum(able) == price:
        print(*able)
        continue
    
    able_sort = []
    for i in range(n):
        able_sort.append((able[i], i))
    # 금액 많은 순, 같은 금액이면 더 앞에 있는 사람 순서
    able_sort.sort(key=lambda x:(-x[0], x[1]))
    
    # 각 사람이 내야하는 금액
    charge = [0] * n
    # 모든 사람이 내는 금액의 합
    sum_price = 0
    # 평등하게 낼 때 금액
    avg_price = price // n
    # 평등 금액을 우선 배분
    for p, idx in able_sort:
        if p >= avg_price:
            charge[idx] = avg_price
            sum_price += avg_price
        else:
            charge[idx] = p
            sum_price += p
    
    # 남은 금액 모두 채우기
    while sum_price < price:
        # 가능한 금액을 모두 사용했으면 제거
        while able_sort:
            if able[able_sort[-1][1]] == charge[able_sort[-1][1]]:
                able_sort.pop()
            else:
                break
        if able_sort == []:
            break
        # 추가적 부담 가능한 금액 / 가장 적은 허용범위 사람 기준으로
        diff = able[able_sort[-1][1]] - charge[able_sort[-1][1]]
        if diff * len(able_sort) <= price - sum_price:
            sum_price += diff * len(able_sort)
            for _, idx in able_sort:
                charge[idx] += diff
        # 남은 사람이 동등하게 분담하고도 남을 때
        else:
            # 전체 남은 양을 동등하게 분배하기
            diff_per_person = (price - sum_price) // len(able_sort)
            sum_price += diff_per_person * len(able_sort)
            for _, idx in able_sort:
                charge[idx] += diff_per_person
            # 남은 개수는 앞에서부터 하나씩만 추가
            for _, idx in able_sort:
                if sum_price == price:
                    break
                charge[idx] += 1
                sum_price += 1
    print(*charge)


'''
# IndexError
for _ in range(int(input())):
    price, n = MIIS()
    able = list(MIIS())
    
    # 모든 사람 가능 금액이 선물 금액 넘는 경우
    if sum(able) < price:
        print('IMPOSSIBLE')
        continue
    # 정확히 금액이 일치하는 경우
    elif sum(able) == price:
        print(*able)
        continue
    
    able_sort = []
    for i in range(n):
        able_sort.append((able[i], i))
    # 금액 많은 순, 같은 금액이면 더 앞에 있는 사람 순서
    able_sort.sort(key=lambda x:(-x[0], x[1]))
    
    # 각 사람이 내야하는 금액
    charge = [0] * n
    # 모든 사람이 내는 금액의 합
    sum_price = 0
    # 평등하게 낼 때 금액
    avg_price = price // n
    # 평등 금액을 우선 배분
    for p, idx in able_sort:
        if p >= avg_price:
            charge[idx] = avg_price
            sum_price += avg_price
        else:
            charge[idx] = p
            sum_price += p
    
    charge_all_idx = n - 1
    # 남은 금액 모두 채우기
    while sum_price < price:
        # 가능한 모든 금액 내지 않은 가장 뒤 인덱스 탐색
        for i in range(charge_all_idx, -1, -1):
            if able[able_sort[i][1]] != charge[able_sort[i][1]]:
                charge_all_idx = i + 1
                break
        diff = able[able_sort[charge_all_idx - 1][1]] - able_sort[charge_all_idx][0]
        if diff * charge_all_idx < price - sum_price:
            sum_price += diff * charge_all_idx
            for i in range(charge_all_idx - 1, -1, -1):
                charge[i] += diff
        else:
            diff_per_person = (price - sum_price) // charge_all_idx
            sum_price += diff_per_person * charge_all_idx
            for i in range(charge_all_idx - 1, -1, -1):
                charge[i] += diff_per_person
            # 남은 개수는 앞에서부터 하나씩만 추가
            left = price - sum_price
            for i in range(n):
                if left == 0:
                    break
                charge[able_sort[i][1]] += 1
                sum_price += 1
                left -= 1
    print(*charge)
'''

'''
1
24 5
7 6 5 4 3
ans : 6 6 5 4 3

1
100 5
97 1 1 1 1

'''
