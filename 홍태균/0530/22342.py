'''
계산 로봇

'''
import sys
input = sys.stdin.readline

M, N = map(int,input().split())

D = [list(map(int,input().strip())) for _ in range(M)]

# 저장 패딩 두고 저장
save = [[0] * (N+2) for _ in range(M+2)]
output = [[0] * (N+2) for _ in range(M+2)]

# 초기화
for i in range(1,M+1):
    output[i][1] = D[i-1][0]

result = 0
# 열 순으로 탐색
for j in range(1,N+1):
    for i in range(1,M+1):
        # 3개 중 가장 큰 거
        save[i][j] = max(output[i-1][j-1],output[i][j-1],output[i+1][j-1])
        # 출력값 저장
        output[i][j] = save[i][j] + D[i-1][j-1]
        # 정답 갱신
        result = max(save[i][j],result)

print(result)