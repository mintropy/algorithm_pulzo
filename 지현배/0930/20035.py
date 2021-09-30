import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Amax = max(A)
Bmax = max(B)
Asum = sum(A) + Amax * (M - 1)
Bsum = sum(B)
Aidx = A.index(Amax)
A.reverse()
Aldx = len(A) - A.index(Amax) - 1
Bsum += B[0] * Aidx + B[-1] * (N - Aldx - 1) + Bmax * (Aldx - Aidx)
print(Asum * 10 ** 9 + Bsum)