import sys

N = int(sys.stdin.readline())
# 일별 최댓값
benefit = [0 for _ in range(N + 2)]
maxBenefit = 0

for i in range(1, N + 1):
    Ti, Pi = map(int, sys.stdin.readline().split())
    # 어제까지의 수입이 오늘보다 크면 덮어씀
    if benefit[i - 1] > benefit[i]:
        benefit[i] = benefit[i - 1]
    # 퇴사일을 넘기면 continue
    if i + Ti > N + 1:
        continue
    # Ti일 후의 수입 비교 후 덮어씀
    benefit[i + Ti] = max(benefit[i] + Pi, benefit[i + Ti])
    # 그리고 총 최댓값에도 덮어씀
    maxBenefit = max(maxBenefit, benefit[i + Ti])
print(maxBenefit)