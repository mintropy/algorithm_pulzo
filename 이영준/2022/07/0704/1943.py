"""
Title : 동전 분배
Link : https://www.acmicpc.net/problem/1943
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    for _ in range(3):
        coins = {}
        coins_sum = 0
        for _ in range(int(input())):
            coin, count = map(int, input().split())
            coins[coin] = count
            coins_sum += coin * count
        if coins_sum % 2:
            print(0)
            continue
        coins_sum //= 2
        dp = [False] * (coins_sum + 1)
        dp[0] = True
        for x, count in coins.items():
            for y in range(coins_sum - 1, -1, -1):
                if not dp[y]:
                    continue
                for k in range(1, count + 1):
                    if y + x * k <= coins_sum:
                        dp[y + x * k] = True
        print(1 if dp[coins_sum] else 0)

"""
윤화 준희, 원장 선생님께 동전 몇개를 받음
원장 선생님께 받은 돈을 어떻게 나누어 할지 고민
돈을 똑같이 나누기

똑같이 나누기 불가능한 경우
"""
