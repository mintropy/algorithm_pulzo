"""
Title : 숫자 연결하기
Link : https://www.acmicpc.net/problem/1323
"""

n, k = map(int, input().split())

# 1번 반복해 적었을 때 나머지
r = n % k

count = 1
remainder = set()
while True:
    if r in remainder:
        print(-1)
        break
    elif not r:
        print(count)
        break
    else:
        remainder.add(r)
        count += 1
        r = int(str(r) + str(n))
        r %= k
