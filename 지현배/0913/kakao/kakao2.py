def solution(n, k):
    answer = 0
    # 소수 판별
    def isPrime(n):
        if n <= 1: return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    # 진수 변환
    def trans(n, k):
        res = []
        while n:
            res.append(n % k)
            n //= k
        return ''.join(res.reverse())
    
    num = trans(n, k)
    stack = []
    for i in range(len(num)):
        # 0이 아니면 스택에 넣고
        if num[i] != '0':
            stack.append(num[i])
        else:
            # 0이 나왔을때 스택이 소수인지 판별
            if isPrime(int(''.join(stack))):
                answer += 1
            stack = []
    # 스택에 남아있는 수가 소수인지 판별
    if stack and isPrime(int(''.join(stack))):
        answer += 1
    return answer