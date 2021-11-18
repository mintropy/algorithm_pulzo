# 모듈러 연산
# (a mod n * b mod n) mod n = (a*b) mod n
# (a mod n + b mod n) mod n = (a+b) mod n

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num = N % K
cnt = 1
N_len = len(str(N))
jarisu = 10 ** N_len

already = set()

while True:
    # print(num)
    if num == 0:
        break


    else:
        num = (N % K + (num * (jarisu % K)) % K) % K  # 예) 100100100100의 나머지 = (100의 나머지 + 100100100000의 나머지)의 나머지

        cnt += 1
        if num in already:
            cnt = -1
            break

        already.add(num)

print(cnt)