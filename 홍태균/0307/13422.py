'''
도둑

'''
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M, K = map(int,input().split())
    
    homes = list(map(int,input().split()))
    
    cnt = 0
    if N == M:
        sum_money = sum(homes)
        if sum_money < K:
            cnt += 1
    else:
        homes += homes
        sum_money = sum(homes[:M])
        i = 0
        
        while i < N:
            if sum_money < K:
                cnt += 1
            
            sum_money = sum_money - homes[i] + homes[i+M]
                  
            i += 1
            
    print(cnt)