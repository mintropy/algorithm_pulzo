"""
Title : 색종이와 가위
Link : https://www.acmicpc.net/problem/20444
"""

n, k = map(int, input().split())

# 원하는 조각 - 최소 조각
diff = k - (n + 1)

if diff == 0:
    print('YES')
elif diff < 0:
    print('NO')
# n이 짝수/홀수 일때로
elif n % 2 == 0:
    T = (n // 2) ** 2 - diff
    if T >= 0 and T == int(T ** 0.5) ** 2:
        print('YES')
    else:
        print('NO')
else:
    T = ((n - 1) // 2 ) * ((n - 1) // 2 + 1) - diff
    if T < 0:
        print('NO')
    else:
        T0 = int(T ** 0.5)
        T1 = T0 + 1
        if T0 * T1 != T:
            print('NO')
        else:
            print('YES')

'''
Counter Example
n == 4일 때, 5, 8, 9 가능
n == 5일 때, 6, 10, 12 가능

1073741824 4611686018427387904

2 4
'''