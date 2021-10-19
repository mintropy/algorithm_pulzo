import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
S = sorted(map(int, input().split()))

for _ in range(K):
    L, R, X = map(int, input().split())
    for i in range(L-1, R):
        S[i] += X
    S.sort()
print(*S)