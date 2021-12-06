"""
Title : 여섯 방정식
Link : https://www.acmicpc.net/problem/9765
"""

def find_gcd(x, y):
    if x < y:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x


c1, c2, c3, c4, c5, c6 = map(int, input().split())

x2 = find_gcd(c1, c5)
x6 = find_gcd(c3, c6)

print(c1 // x2, x2, c5 // x2, c6 // x6, x6, c3 // x6)


"""
# 전체 탐색
'''
1. c1 = x1 * x2
2. x4 = c4 * x1
3. c3 = x6 * x7
4. x8 = x7 * c2
5. c5 = x2 * x3
6. c6 = x6 * x5

1, 5번 식과 3, 6번식
1, 5 >> x1, x2, x3
3, 6 >> x5, x6, x7
'''

c1, c2, c3, c4, c5, c6 = map(int, input().split())

# x1, x2, x3, x5, x6, x7
x = [0] * 6

if not c5 % 2 and not c1 % 2:
    # x2
    x[1] = 2
    # x1
    x[0] = c1 // 2
    # x3
    x[2] = c5 // 2
if not c3 % 2 and not c6 % 2:
    # x6
    x[4] = 2
    # x5
    x[3] = c6 // 2
    # x7
    x[5] = c3 // 2

for i in range(3, 20_000_001, 2):
    if all(x):
        break
    if not x[0] and not c5 % i and not c1 % i:
        # x2
        x[1] = i
        # x1
        x[0] = c1 // i
        # x3
        x[2] = c5 // i
    if not x[3] and not c3 % i and not c6 % i:
        # x6
        x[4] = i
        # x5
        x[3] = c6 // i
        # x7
        x[5] = c3 // i

print(*x)
"""
