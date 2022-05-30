"""
Title : 신기한 소수
Link : https://www.acmicpc.net/problem/2023
"""

from sys import stdin

input = stdin.readline


def is_prime(x: int) -> bool:
    if x == 1:
        return False
    for d in range(2, int(x**0.5) + 1):
        if not x % d:
            return False
    return True


def find_magic_prime(N: int, num: int) -> None:
    global is_prime
    if N == 1:
        print(num)
        return
    for x in range(1, 10, 2):
        y = num * 10 + x
        if is_prime(y):
            find_magic_prime(N - 1, y)


if __name__ == "__main__":
    N = int(input())
    for x in 2, 3, 5, 7:
        find_magic_prime(N, x)
