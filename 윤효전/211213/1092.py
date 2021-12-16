import sys
#sys.stdin = open("testcases/1.in", 'r')
#input = sys.stdin.readline

# 1 <= N <= 50
# 1 <= M <= 10,000
# 1 <= weight <= 1,000,000

N = int(input())
S = list(map(int, input().split()))

M = int(input())
S2 = list(map(int, input().split()))

S.sort()
S2.sort()

if S[-1] < S2[-1]:
    print(-1)
    exit()

l = [0]*N
i, j = 0, 0
while j < M:
    if S2[j] <= S[i]:
        l[i] += 1
        j += 1
    else:
        i += 1

p = [i for i in range(N)]

ans = 0
hap = sum(l)
while hap > 0:
    for i in range(N):
        if l[p[i]] > 0 and p[i] >= 0:
            l[p[i]] -= 1
            hap -= 1
        else:
            while l[p[i]] == 0 and p[i] >= 0:
                p[i] -= 1
            if p[i] >= 0:
                l[p[i]] -= 1
                hap -= 1
    ans += 1

print(ans)