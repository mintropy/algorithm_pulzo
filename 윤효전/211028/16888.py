import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

l = []
i = 1
while i**2 <= 1000000:
    l.append(i**2)
    i += 1

dp = [0] * 1000001
for i in range(1, 1000001):
    for v in l:
        if i-v == 0:
            dp[i] = 1
        elif i-v > 0:
            if dp[i-v] == 0:
                dp[i] = 1
                break
        else:
            break
    #print(f'{i} {dp[i]}')


T = int(input())
for _ in range(T):
    N = int(input())
    if dp[N] == 1:
        print('koosaga')
    else:
        print('cubelover')
