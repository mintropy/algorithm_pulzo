import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

SIZE = 501

b = tuple(map(int, input().split()))
dp = [[0]*SIZE for _ in range(SIZE)]

for v in b:
    dp[0][v] = 1

for i in range(SIZE):
    for j in range(i, SIZE):
        for k in range(3):
            tmp1, tmp2 = i-b[k], j
            if tmp1 > tmp2:
                tmp1, tmp2 = tmp2, tmp1
            if tmp1 >= 0 and tmp2 >= 0:
                if dp[tmp1][tmp2] == 0:
                    dp[i][j] = 1
                    break

            tmp1, tmp2 = i, j-b[k]
            if tmp1 > tmp2:
                tmp1, tmp2 = tmp2, tmp1
            if tmp1 >= 0 and tmp2 >= 0:
                if dp[tmp1][tmp2] == 0:
                    dp[i][j] = 1
                    break


for i in range(5):
    k1, k2 = map(int, input().split())
    if k1 > k2:
        k1, k2 = k2, k1
    if dp[k1][k2] == 1:
        print('A')
    else:
        print('B')
