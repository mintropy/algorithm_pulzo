"""
Title : IPv6
Link : https://www.acmicpc.net/problem/3107
"""

import sys
input = sys.stdin.readline


short_IPv6 = list(input().strip().split(':'))
long_IPv6 = []

# 2번 규칙이 적용된 경우
# 더 적다면 채워주기
if len(short_IPv6) < 8:
    tmp_IPv6 = []
    while short_IPv6:
        if short_IPv6[-1]:
            tmp_IPv6.append(short_IPv6.pop())
        else:
            while True:
                if not short_IPv6 or short_IPv6[-1]:
                    break
                else:
                    short_IPv6.pop()
            add = len(tmp_IPv6) + len(short_IPv6)
            tmp_IPv6 += ['0000'] * ( 8 - add)
            tmp_IPv6 += short_IPv6[::-1]
            break
    tmp_IPv6.reverse()
    short_IPv6 = tmp_IPv6[::]
# 더 많다면 하나가 제거된 것 (:0000: >> :::)
elif len(short_IPv6) > 8:
    tmp_IPv6 = []
    check = False
    for IP in short_IPv6:
        if IP:
            tmp_IPv6.append(IP)
        elif not check:
            tmp_IPv6.append(IP)
            check = True
    short_IPv6 = tmp_IPv6[::]

# 1번 규칙 적용
for IP in short_IPv6:
    long_IPv6.append(IP.zfill(4))

print(':'.join(long_IPv6))
