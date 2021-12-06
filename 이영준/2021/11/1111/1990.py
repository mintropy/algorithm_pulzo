"""
Title : 소수인팰린드롬
Link : https://www.acmicpc.net/problem/1990
"""

import sys
input = sys.stdin.readline


def find_palindrome_num(st: int, end: int):
    palindrome_nums = []
    if st <= 5 <= end:
        palindrome_nums.append(5)
    if st <= 7 <= end:
        palindrome_nums.append(7)
    if st <= 11 <= end:
        palindrome_nums.append(11)
    for num in range(1, 1000):
        for single_num in range(10):
            new_palin_num = int(str(num) + str(single_num) + str(num)[::-1])
            if new_palin_num > end:
                return palindrome_nums
            if st <= new_palin_num and new_palin_num % 2:
                palindrome_nums.append(new_palin_num)
    return palindrome_nums


a, b = map(int, input().split())

is_prime = [True] * (int(b ** 0.5) + 1)
primes = []
for i in range(2, int(b ** 0.5) + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, int(b ** 0.5) + 1, i):
            is_prime[j] = False


palindrome_nums = find_palindrome_num(a, b)
for palin_num in palindrome_nums:
    for prime in primes:
        if prime * prime > palin_num:
            print(palin_num)
            break
        if palin_num % prime == 0:
            break
    else:
        print(palin_num)
else:
    print(-1)


'''
# python TLE
def is_prime_num(num: int, primes: list) -> bool:
    for prime in primes:
        if prime * prime > num:
            return True
        if num % prime == 0:
            return False
    return True


def is_pal(num: str) -> bool:
    if str(num) == str(num)[::-1]:
        return True
    return False


a, b = map(int, input().split())
b = min(b, 10 ** 8)

is_prime = [True] * (int(b ** 0.5) + 1)
primes = []
for i in range(2, int(b ** 0.5) + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, int(b ** 0.5) + 1, i):
            is_prime[j] = False

ans = []

# 10 ** 8 ~ 10 ** 9사이 소수 팰린드롬 없음
if a <= 2 <= b:
    ans.append(2)
    a = 3
else:
    a = (a // 2) * 2 + 1

for num in range(a, b + 1, 2):
    if is_pal(str(num)) and is_prime_num(num, primes):
        ans.append(num)
else:
    ans.append(-1)

print(*ans, sep='\n')
'''