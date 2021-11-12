import sys
input = sys.stdin.readline

# 카탈랑 수
# Cn = (2n)!/n!(n+1)!
# C0 = 1
# Cn = sig(i=0~n-1)CiCn-1-i
C = [1]
for i in range(1, 31):
    tmp = 0
    for j in range(i):
        tmp += C[j] * C[i - j - 1]
    C.append(tmp)

while True:
    N = int(input())
    if N == 0:
        break
    print(C[N])