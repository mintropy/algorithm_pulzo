import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
malfuncBtns = []
if M:
    malfuncBtns = list(input().split())

res = abs(N - 100)

low = high = N
while low >= 0 or high <= 1000000:
    if low >= 0:
        lowTarget = str(low)
        lowSize = len(lowTarget)
        for lt in lowTarget:
            if lt in malfuncBtns:
                break
        else:
            clkCnt = abs(N - low) + lowSize
            res = min(res, clkCnt)
            break
        low -= 1

    if high <= 1000000:
        highTarget = str(high)
        highSize = len(highTarget)
        for ht in highTarget:
            if ht in malfuncBtns:
                break
        else:
            clkCnt = abs(N - high) + highSize
            res = min(res, clkCnt)
            break
        high += 1
print(res)