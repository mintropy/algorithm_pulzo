def sol():
    N, P, K, D = map(int, input().split())

    scores = [0] * N
    # 서로 다른 D 개의 점수를 만들 수 없으면 wrong
    if D * (D - 1) // 2 > P:
        return []
    # 상위 K 명의 점수가 모두 동일할 때
    if D == 1:
        # 그 K와 전체 학생 수가 같고
        if N == K:
            # 전체 점수가 전체 학생 수로 나누어 떨어지지 않으면 wrong
            if P % K:
                return []
        # 전체 학생수가 K와 안 같으면
        else:
            # K번째 학생에게 점수 몰빵
            scores[K] = P % K
        # 그 몰빵한 점수가 상위애들 점수보다 크면 wrong
        if P // K < P % K:
            return []
        # 그 외의 경우 상위 K 명에게 균등 분배
        for i in range(K):
            scores[i] = P // K
        return scores
    # D 가 1 보다 크면 가장 높은 학생부터 1씩 줄여가며 점수 주고
    for i in range(D):
        scores[i] = D - i - 1
    # 남은 만큼 1등에게 몰빵
    scores[0] += P - (D * (D - 1) // 2)
    return scores
arr = sol()
if not arr:
    print('Wrong information')
else:
    print(*arr, sep='\n')