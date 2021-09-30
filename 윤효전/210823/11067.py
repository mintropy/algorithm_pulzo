import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    S = [(-1, 0)] + sorted([tuple(map(int, input().split()))
                            for _ in range(N)])
    _, *M = map(int, input().split())

    for i in range(1, N+1):
        if S[i][0] != S[i-1][0] and S[i][1] != S[i-1][1]:
            start = i
            end = i
            tmp = i
            target = S[i][0]
            while True:
                tmp += 1
                if tmp >= len(S):
                    break
                if S[tmp][0] == target:
                    end = tmp
                else:
                    break

            lim = (end-start+1)//2
            for j in range(lim):
                S[start+j], S[end-j] = S[end-j], S[start+j]

    for m in M:
        print(*S[m])
