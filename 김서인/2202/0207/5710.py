import sys

input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    # 적은 사람의 전기 사용량 기준으로 이분 탐색하기
    left = 0
    right = A

    while left <= right:
        mid = (left + right) // 2
        a = mid  # 상근이가 내는 전기 요금
        # 상근이가 쓴 전기 사용량 계산
        a_mount = 0
        if 200 >= a >= 1:
            a_mount += (a / 2)
        elif 29900 >= a > 200:
            a -= 200
            a_mount = 100 + (a) / 3
        elif 4_979_900 >= a > 29900:
            a -= 29900
            a_mount = 10000 + (a) / 5
        elif a > 4_979_900:
            a -= 4_979_900
            a_mount = 1000000 + (a) / 7

        b = mid + B  # 다른 이웃이 내는 전기 요금
        b_mount = 0  # 다른 이웃이 내는 전기 사용량 계산
        if 200 >= b >= 1:
            b_mount += (b / 2)
        elif 29900 >= b > 200:
            b -= 200
            b_mount = 100 + (b) / 3
        elif 4_979_900 >= b > 29900:
            b -= 29900
            b_mount = 10000 + (b) / 5
        elif b > 4_979_900:
            b -= 4_979_900
            b_mount = 1000000 + (b) / 7

        # 상근이와 이웃이 사용한 전기 사용량을 합쳤을 때 내야 하는 요금 계산하기
        a_b_sum_mount = a_mount + b_mount
        a_b_sum = 0

        if 100 >= a_b_sum_mount >= 1:
            a_b_sum += (a_b_sum_mount * 2)
        elif 10000 >= a_b_sum_mount >= 100:
            a_b_sum_mount -= 100
            a_b_sum = 200 + (a_b_sum_mount) * 3
        elif 1000000 >= a_b_sum_mount > 10000:
            a_b_sum_mount -= 10000
            a_b_sum = 29900 + (a_b_sum_mount) * 5
        elif a_b_sum_mount > 1000000:
            a_b_sum_mount -= 1000000
            a_b_sum = 4979900 + (a_b_sum_mount) * 7

        # A와 계산 결과가 같은지 보기
        if A == a_b_sum:
            print(mid)
            break
        elif A > a_b_sum:
            left = mid + 1
        else:
            right = mid - 1
