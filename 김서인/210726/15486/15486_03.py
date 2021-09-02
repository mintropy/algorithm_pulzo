import sys
input = sys.stdin.readline

# 입력받기
n = int(input())

info = []
for i in range(n):
    a, b = map(int,input().split())
    info.append((a,b))
#print(info)

# 각 날에 최대로 벌 수 있는 돈
dy = [0] * (n+1000)

for i in range(n):
    period, money = info[i]
    dy[i] = max(dy[i], dy[i-1]) # 전날이 더 크면, 전날 것으로 ..! 
    dy[i+period] = max(dy[i+period], dy[i]+money)  # 상담 안한 경우, 상담 한 경우


dy[n] = max(dy[n], dy[n-1]) # 전날이 더 크면, 전날 것으로 ..! 

# print(dy)
print(dy[n])