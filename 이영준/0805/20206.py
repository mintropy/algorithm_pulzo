"""
Title : 푸앙이가 길을 건너는 이유
Link : https://www.acmicpc.net/problem/20206
"""

a, b, c = map(int, input().split())
x1, x2, y1, y2 = map(int, input().split())


if a * b < 0:
    y1, y2 = y2, y1

r1 = x1 * a + y1 * b + c
r2 = x2 * a + y2 * b + c
result = r1 * r2

if result >= 0:
    print('Lucky')
else:
    print('Poor')


'''
# a 또는 b가 0인 경우
if a == 0:
    # y = - c / b 형태
    # y1 < - c / b < y2 이면 못지나감
    # >> y1 * b < -c < y2 * b
    if b > 0:
        if y1 * b < -c < y2 * b:
            print('Poor')
        else:
            print('Lucky')
    else:
        if y1 * b > -c > y2 * b:
            print('Poor')
        else:
            print('Lucky')
elif b == 0:
    # x = - c / a 형태
    # x1 < - c / a < x2 이면 못지나감
    # >> x1 * a < -c < x2 * a
    if a > 0:
        if x1 * a < -c < x2 * a:
            print('Poor')
        else:
            print('Lucky')
    else:
        if x1 * a > -c > x2 * a:
            print('Poor')
        else:
            print('Lucky')
else:
    # 나머지 경우
    # 기울기가 양수 / 음수인 경우로 구분
    if a * b < 0:
        y1, y2 = y2, y1
    r1 = a * x1 + b * y1 + c
    r2 = a * x2 + b * y2 + c
    ans = r1 * r2
    if ans >= 0:
        print('Lucky')
    else:
        print('Poor')
'''