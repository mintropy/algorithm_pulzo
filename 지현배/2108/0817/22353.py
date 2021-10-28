def sol():
    A, D, K = map(int, input().split())
    # 최종 기댓값은 각 시퀀스의 결과의 합으로 구해진다.
    # 결과는 확률과 그 승부까지 걸린 시간의 곱으로 구해진다.
    # 확률은 2판 전 확률과 (1 - 한 판 전 승률) 그리고 이번판 승률의 곱으로 구해진다.
    # 이번판 승률은 1판 전 승률과 (1 + 상승률)의 곱으로 구해진다.

    # 첫번째 판의 승률, 확률, 결과를 구한다.

    # 0번째 판의 확률에 (1 - 첫번째 판의 승률)을 곱한 값
    prev_prob = 1 - D / 100
    # 첫번째 판의 확률
    probability = D / 100
    # 첫번째 판의 승률
    rate = D / 100
    # 승률의 상승률
    raise_rate = (100 + K) / 100
    # 첫번재 판의 기댓값
    res = A * D / 100
    # 두번째 판까지 걸린 시간
    cnt = 2
    # 승률이 1이상이 될때 까지
    while rate < 1:
        # 승률이 오른다.
        rate *= raise_rate
        # 그 승률이 1이 넘으면 1로 만들어준다.
        if rate > 1:
            rate = 1
        # 2판전 확률에 (1 - 한 판 전 승률)을 곱한 값에 승률을 곱한다.
        probability = prev_prob * rate
        # (1 - 한 판 전 승률)에 (1 - 이번판 승률)을 곱한다.
        prev_prob = prev_prob * (1 - rate)
        # 결과에 값을 누적한다.
        res += cnt * A * probability
        cnt += 1
    return res

print(sol())