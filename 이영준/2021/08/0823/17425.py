"""
Title : 약수의 합
Link : https://www.acmicpc.net/problem/17425
"""

import sys
input = sys.stdin.readline


sum_of_divisor = [1] * (10 ** 6 + 1)
for i in range(2, 10 ** 6 + 1):
    for j in range(i, 10 ** 6 + 1, i):
        sum_of_divisor[j] += i
    sum_of_divisor[i] += sum_of_divisor[i - 1]

for _ in range(int(input())):
    print(sum_of_divisor[int(input())])


'''
f_x = [0] * 1_000_001
for i in range(1, 1_000_001):
    for j in range(i, 1_000_001, i):
        f_x[j] += i
    f_x[i] += f_x[i - 1]

for _ in range(int(input())):
    print(f_x[int(input())])
'''


'''
# 너무 느림
is_prime = [True] * (1000001)
prime = []
for i in range(2, 1000000 + 1):
    if is_prime[i]:
        prime.append(i)
        for j in range(2 * i, 1000000 + 1, i):
            is_prime[j] = False

g_x = [0]
for i in range(1, 1000001):
    divisors = {}
    for p in prime:
        if i == 1:
            break
        if i % p == 0:
            divisors[p] = 1
            i //= p
            while True:
                if i % p != 0:
                    break
                divisors[p] += 1
                i //= p
    
    sum_of_divisors = 1
    for divisor in divisors:
        tmp = 1
        for i in range(divisors[divisor]):
            tmp += divisor ** (i + 1)
        sum_of_divisors *= tmp
    
    g_x.append(sum_of_divisors + g_x[-1])


for _ in range(int(input())):
    n = int(input())
    print(g_x[n])
'''