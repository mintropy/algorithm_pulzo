import sys, collections

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

MAXIMUM = int(100001 ** 0.5) + 1

# 소수들 미리 구하기
primes = [True] * (MAXIMUM)

primes[0] = False
primes[1] = False

sosus = []
# 에라토스테네스의 체
for i in range(2, MAXIMUM):
    if primes[i] == True:
        sosus.append(i)
        for j in range(i * i, MAXIMUM, i):
            primes[j] = False


def makePrimes(num, operator):
    sosu_idx = 0
    while sosu_idx < len(sosus):  # 소수 중에서
        if num == 1 :
            return

        # 자기보다 크면 break
        sosu = sosus[sosu_idx]
        if sosu > num:
            return

        if num % sosu == 0:
            num = num // sosu
            if operator == 0:  # 분자 부분
                primes_cnt[sosu] += 1 # 인수 있으면 그 갯수만큼 primes_cnt에 더하기

            elif operator == 1:  # 분모 부분
                primes_cnt[sosu] -= 1  # 인수 개수만큼 prime_cnt에서 빼기

        else:
            sosu_idx += 1

    # 가능한 소수로 안 나눠지면 원래 소수
    else:
        if operator == 0:
            primes_cnt[num] += 1
        else:
            primes_cnt[num] -= 1

N = int(input())
arr = list(input().split())
mode = 0  # 0: 분자, 1: 분모

primes_cnt = collections.defaultdict(int) # 소수들의 개수를 담음
if int(arr[0]) == 0:
    zero_flag = True

else:
    makePrimes(int(arr[0]), 0)  # 첫번째 수
    zero_flag = False
    for i in range(1, N):  # 이전 기호 / 두번째 수부터
        operator = arr[i * 2 - 1]
        num = abs(int(arr[i * 2]))  # 음수 여부는 정수 ,유리수 판단에 상관없으니 양수로 바꿈.

        if num == 0:
            zero_flag = True
            break

        if operator == '/':
            mode = 1
        else:
            mode = 0

        makePrimes(num, mode)

if zero_flag == True:  # 0이 곱해지면 항상 정수!
    print('mint chocolate')
else:
    for n in primes_cnt.items():
        if n[1] < 0:  # 분모에 1 아닌 수 남아 있다는 것 - 유리수
            print('toothpaste')
            break
    else:  # break 없이 끝까지 갔으면 정수
        print('mint chocolate')
