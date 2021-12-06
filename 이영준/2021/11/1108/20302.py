"""
Title : 민트 초코
Link : https://www.acmicpc.net/problem/20302
"""

import sys
input = sys.stdin.readline


def divide_by_primes(count_primes: dict, primes: list, num: int, plus: bool) -> dict:
    for prime in primes:
        # 1이면 더 연산할 필요 없음
        if num == 1:
            return count_primes
        while not num % prime:
            num //= prime
            if plus:
                count_primes[prime] += 1
            else:
                count_primes[prime] -= 1
    # 가능한 모든 소수로 나누어 안되면 이미 소수
    else:
        if num in count_primes:
            if plus:
                count_primes[num] += 1
            else:
                count_primes[num] -= 1
        else:
            if plus:
                count_primes[num] = 1
            else:
                count_primes[num] = -1
    return count_primes


is_prime = [True] * (int(100_001 ** 0.5) + 1)
primes = []
for i in range(2, int(100_001 ** 0.5) + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, int(100_001 ** 0.5) + 1, i):
            is_prime[j] = False

N = int(input())
# 가장 앞의 수를 분자로 처리하기 위해 * 하나 붙여서 만들기
equation = ['*'] + list(input().strip().split())
# 분모 / 분자일 때 따로 구하지 않고, 분자면 더하고 분모면 빼주기
count_primes = {i: 0 for i in primes}
for i in range(N):
    num = abs(int(equation[i * 2 + 1]))
    # 0이 곱해지면 더 탐색하지 않아도 됨
    if num == 0:
        count_primes[0] = 1
        break
    # 각 수는 양수로 처리하여 확인
    if equation[i * 2] == '*':
        count_primes = divide_by_primes(count_primes, primes, num, True)
    else:
        count_primes = divide_by_primes(count_primes, primes, num, False)

if 0 in count_primes:
    print('mint chocolate')
else:
    for p in count_primes:
        if count_primes[p] < 0:
            print('toothpaste')
            break
    else:
        print('mint chocolate')


'''
# TLE
is_prime = [True] * (100_001)
primes = []
for i in range(2, 100_001):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, 100_001, i):
            is_prime[j] = False


N = int(input())
# 가장 앞의 수를 분자로 처리하기 위해 * 하나 붙여서 만들기
equation = ['*'] + list(input().strip().split())

numerator_list = []
denominator_list = []
zero = False
for i in range(N):
    # 각 수는 양수로 처리하여 확인
    if equation[i * 2] == '*':
        # 분자에 0이 있으면 따로 추가
        if not int(equation[i * 2 + 1]):
            zero = True
        else:
            numerator_list.append(abs(int(equation[i * 2 + 1])))
    else:
        denominator_list.append(abs(int(equation[i * 2 + 1])))

# 분자에 0이 곱해지면 정수
if zero:
    print('mint chocolate')
# 아니라면 검증
else:
    for prime in primes:
        # 분자는 없고 분모만 남은 경우
        if not numerator_list and denominator_list:
            print('toothpaste')
            break
        # 모든 분모가 확인되고 분자만 남은 경우
        if not denominator_list:
            print('mint chocolate')
            break
        next_numerator_list = []
        next_denominator_list = []
        numerator_count = denominator_count = 0
        for num in numerator_list:
            while not num % prime:
                num //= prime
                numerator_count += 1
            if num != 1:
                next_numerator_list.append(num)
        for num in denominator_list:
            while not num % prime:
                num //= prime
                numerator_count += 1
            if num != 1:
                next_denominator_list.append(num)
        # 해당 소수가 분모에 더 많은 경우
        if numerator_count < denominator_count:
            print('toothpaste')
            break
        numerator_list = next_numerator_list[::]
        denominator_list = next_denominator_list[::]
    else:
        print('mint chocolate')
'''

'''
# TLE
def verify(primes: list, numerator: int, denominator: int) -> bool:
    # 각각 prime으로 나누어가며 확인
    for prime in primes:
        # 분모가 1이면 가능 / 종료
        if denominator == 1:
            return True
        while True:
            if not denominator % prime:
                # 분모만 나누어지면 불가능 / 종료
                if numerator % prime:
                    return False
                # 분자 & 분모 둘 다 나눌 수 있으면 나누기
                else:
                    denominator //= prime
                    numerator //= prime
            else:
                break


is_prime = [True] * (100_001)
primes = []
for i in range(2, 100_001):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, 100_001, i):
            is_prime[j] = False


N = int(input())
equation = ['*'] + list(input().strip().split())

# 모든 분자 / 분모를 각각에 곱하여 저장
numerator = denominator = 1
for i in range(N):
    if equation[i * 2] == '*':
        numerator *= int(equation[i * 2 + 1])
    else:
        denominator *= int(equation[i * 2 + 1])
# 모두 양수로 저장
numerator = abs(numerator)
denominator = abs(denominator)

if not numerator or verify(primes, numerator, denominator):
    print('mint chocolate')
else:
    print('toothpaste')
'''

'''
# TLE
def divide_by_primes(prime_dict: dict, primes: list, num: int) -> dict:
    for prime in primes:
        if abs(num) == 1:
            break
        while True:
            if num % prime:
                break
            num //= prime
            prime_dict[prime] += 1
    return prime_dict


is_prime = [True] * (100_001)
primes = []
for i in range(2, 100_001):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, 100_001, i):
            is_prime[j] = False


N = int(input())
equation = ['*'] + list(input().strip().split())


# 각각 분자/분모 확인
# 각각의 수가 어떻게 소인수 분해 될 수 있는지로 모든 수 담기
numerator = {i: 0 for i in primes}
denominator = {i: 0 for i in primes}

# 한번에 2개씩 확인
# *면 분자에, /면 분모에 추가하기
for i in range(N):
    if equation[i * 2] == '*':
        numerator = divide_by_primes(numerator, primes, int(equation[i * 2 + 1]))
    else:
        denominator = divide_by_primes(denominator, primes, int(equation[i * 2 + 1]))

# 각각 prime을 확인하면서 분모에 더 많으면 정수 불가능
for prime in primes:
    if numerator[prime] < denominator[prime]:
        print('toothpaste')
        break
else:
    print('mint chocolate')
'''