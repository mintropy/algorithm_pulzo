'''
초콜릿 뺏어 먹기

'''
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
chocolates = list(map(int,input().split()))

# 날짜와 갯수
days = 0
cnt = 0
# 가장 작은 수의 초콜렛(목표 초콜렛 수)
fix_choco = chocolates[0]

# 결국 모든 상자와 비교하게 되기 때문에 
# 처음 상자를 제외하고 비교
for i in range(1,N):
    # 다르다면 그만큼 초콜렛을 빼게 되고 
    # 하루가 흐른다
    if chocolates[i] != fix_choco:
        cnt += (chocolates[i] - fix_choco)
        days += 1

print(cnt, days)