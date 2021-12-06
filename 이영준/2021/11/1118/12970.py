"""
Title : AB
Link : https://www.acmicpc.net/problem/12970
"""

N, K = map(int, input().split())

if K > (N // 2) * (N - N // 2):
    print(-1)
elif K < N:
    print('B' * (N - K - 1) + 'A' + 'B' * K)
else:
    for i in range(1, N // 2 + 1):
        if i * (N - i) == K:
            print('A' * i + 'B' * (N - i))
            break
        elif i * (N - i - 1)  <= K <= i * (N - i - 1) + (N - i - 1):
            res = K - i * (N - i - 1)
            print('A' * i + 'B' * (N - i - res - 1) + 'A' + 'B' * res)
            break


'''
N = 5일 때
K = 5, ABABB

N = 6일 때
K = 6, ABBABB
K = 7, ABABBB
K = 8, AABBBB

N = 7일 때
A를 최소로 사용해도 3개는 필요한 경우 발생
K = 11, AABABBB
'''