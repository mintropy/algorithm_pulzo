"""
Title : 지금 만나러 갑니다
Link : https://www.acmicpc.net/problem/18235
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, A, B = map(int ,input().split())
    ans = -1
    duck_A, duck_B = {A}, {B}
    day, power = 0, 1
    while power <= N:
        if duck_A & duck_B:
            ans = day
            break
        next_duck_A, next_duck_B = set(), set()
        for a in duck_A:
            if a - power > 0:
                next_duck_A.add(a - power)
            if a + power <= N:
                next_duck_A.add(a + power)
        for b in duck_B:
            if b - power > 0:
                next_duck_B.add(b - power)
            if b + power<= N:
                next_duck_B.add(b + power)
        duck_A, duck_B = next_duck_A, next_duck_B
        day += 1
        power *= 2
    print(ans)
