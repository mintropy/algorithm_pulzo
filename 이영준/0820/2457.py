"""
Title : 공주님의 정원
Link : https://www.acmicpc.net/problem/2457
"""

import sys
input = sys.stdin.readline


def check(m1, d1, m2, d2):
    # 비교 기준으로 할 날짜 m1, d1
    # 가능한지 확인할 날짜 m2, d2
    # m1, d1이 더 빠르거나 같은지 확인
    # 가능한 경우만 고르고, 아니면 False
    if m1 < m2:
        return True
    elif m1 == m2 and d1 <= d2:
        return True
    return False


n = int(input())
flowers = [tuple(map(int, input().split())) for _ in range(n)]

flowers.sort(key = lambda x:(-x[2], -x[3], x[0], x[1]))

# 가장 늦게 지는 꽃이 11월 30일까지 펴있는지 확인
if flowers[0][2] <= 11:
    print(0)
# 꽃을 모두 꺼내며 확인
else:
    flower_count = 1
    m1, d1, m2, d2 = flowers[0]
    # 마지막에 지는 꽃이 피는 날짜
    blossom = [m1, d1]
    # 그 전에 선택할 꽃 예비 명단
    prob = []
    idx = 0
    for i in range(1, n):
        # 12월에 지는 꽃일때 확인 필요
        # 12월 꽃인경우 모두 확인
        if flowers[i][2] == 12:
            # 꽃이 더 빨리 핀다면 바꾸기
            if check(*flowers[i][:2], *blossom):
                blossom = flowers[i][:2]
        else:
            idx = i
            break
    # 12월에 피는 꽃이 아닐때부터 탐색 시작
    for i in range(idx, n):
        m1, d1, m2, d2 = flowers[i]
        # 피는날 지는날 같은 경우 없음
        # 피는날 지는날 같으면 넘어가기
        # if m1 == m2 and d1 == d2:
        #     continue
        # 만약 지금꽃이 3월 1일 이전에 핀다면 종료
        if prob and check(*blossom, 3, 1):
            print(flower_count)
            break
        # 해당 꽃이 가능하면 예비명단과 비교 최신화
        if check(*blossom, m2, d2):
            if not prob:
                prob = [m1, d1]
            # 예비 명단의 꽃보다 더 빨피 피는지 확인
            elif check(m1, d1, *prob):
                prob = [m1, d1]
            else:
                continue
        # 불가능하면, 예비명단 꽃을 최신꽃으로
        else:
            flower_count += 1
            blossom = prob
            # 바뀐 꽃과 비교해서 가능한지 다시 확인
            if check(*blossom, m2, d2):
                prob = [m1, d1]
            else:
                print(0)
                break
    else:
        # 모든 꽃을 확인한 경우, 지금꽃, 예비꽃을 확인
        # 마지막에 지금꽃이 된경우 꽃 확인 개수 출력
        # 마지막까지 지금꽃으로 안되고, 예비꽃이 되는 경우
        # 꽃 확인개수 + 1 출력
        if check(*blossom, 3, 1):
            print(flower_count)
        elif check(*prob, 3, 1):
            print(flower_count + 1)
        else:
            print(0)



'''
Counter Example
10
1 1 11 23
11 22 11 24
11 23 11 25
11 24 11 26
11 25 11 27
11 26 11 28
11 27 11 29
11 28 12 1
11 23 11 27
11 27 12 1
ans : 3
output : 2


3
11 1 12 1
3 1 11 2
1 1 3 5
'''