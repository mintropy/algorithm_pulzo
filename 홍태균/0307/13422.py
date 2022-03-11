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
    # N과 M이 같다면
    # 다 더해서 확인
    if N == M:
        sum_money = sum(homes)
        if sum_money < K:
            cnt += 1
    else:
        # 인덱스 넘는것을 방지하기 위해서
        homes += homes
        # 처음 M개 집 합
        sum_money = sum(homes[:M])
        i = 0
        
        while i < N:
            if sum_money < K:
                cnt += 1
            # 앞에 집은 빼고 뒤에 집은 더하는 방식
            sum_money = sum_money - homes[i] + homes[i+M]
                  
            i += 1
            
    print(cnt)