'''
전기 요금

'''
import sys
input = sys.stdin.readline

# 요금 구하기
def account(N):
    
    if N <= 100:
        return N * 2
    elif N < 10000:
        return 100 * 2 + (N-100) * 3
    elif N < 1000000:
        return 100 * 2 + 9900 * 3 + (N-10000) * 5
    else:
        return 100 * 2 + 9900 * 3 + 990000 * 5 + (N-1000000) * 7

while 1:
    A, B = map(int,input().split())
    # 끝
    if A == B == 0:
        break
    # 사용량 구하기
    if A <= 200:
        Wh = A//2
    elif A <= 2*100 + 3*9900:
        Wh = 100 + (A-2*100)//3
    elif A <= 2*100 + 3*9900 + 5*990000:
        Wh = 10000 + (A-2*100-3*9900)//5
    else:
        Wh = 1000000 + (A-2*100-3*9900-5*990000)//7
    # 가장 작은 사용량은 1
    # 이웃보다 무조건 작기 때문에 가장 큰 사용량은 사용량의 반 
    l = 1
    r = Wh//2
    
    while l <= r:
        # 내 사용량
        mid = (l+r)//2
        # 이웃 사용량
        Ne = Wh - mid
        # 요금차이
        diff = account(Ne) - account(mid)
        # B와 비교 
        if diff > B:
            l = mid + 1
        else:
            r = mid - 1
    
    print(account(l))
        