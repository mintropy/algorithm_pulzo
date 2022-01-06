import sys
input = sys.stdin.readline

dp = [0,1,2]

while True:
    tmp = dp[-1]+dp[-2]
    if tmp <= 1_000_000_000_000_000_000:
        dp.append(tmp)
    else:
        break
    
K = int(input())
idx = len(dp)-1
flag = False
while idx:
    if K >= dp[idx]:
        K -= dp[idx]
        flag = True
        print(1, end='')
    else:
        if flag:
            print(0, end='')
    idx -= 1