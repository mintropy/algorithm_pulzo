def solution(n, k):
    # k가 10이 아닐 때 k진수로 변환
    if k != 10:
        num = []
        while n:
            num.append(n % k)
            n //= k
        num.reverse()
    # k가 10이면 그대로 리스트로 변환
    else:
        num = list(int(i) for i in str(n))
    # 0으로 구분, 정답 가능성이 있는 수
    prob = []
    tmp = 0
    for m in num:
        if m:
            tmp *= 10
            tmp += m
        else:
            if tmp:
                prob.append(tmp)
                tmp = 0
    else:
        if tmp:
            prob.append(tmp)
    
    # 소수 확인
    if len(prob) >= 2:
        is_prime = [True] * (max(prob) + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, len(is_prime)):
            if is_prime[i]:
                for j in range(i * 2, len(is_prime), i):
                    is_prime[j] = False
        
        answer = 0
        for m in prob:
            if is_prime[m]:
                answer += 1
        
        return answer
    # 가능한 수가 하나라면, 그 수가 매우 커질 수 있기때문에 따로 계산
    else:
        m = prob[0]
        for k in range(2, int(m ** 0.5) + 1):
            if not m % k:
                return 0
        return 1