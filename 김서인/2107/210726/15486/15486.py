import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())

finish_days = [0]
prices = [0]

for i in range(n):
    a, b = map(int,input().split())
    finish_days.append(a+i)
    prices.append(b)

# 각 날짜를 인덱스로 해서, 가장 최대 이익을 얻을 수 있을 때의 금액을 get_moneys에 저장.
get_moneys = [0]*(n+51)
get_moneys[finish_days[1]] = prices[1]
res = 0

for i in range(1, n + 1): # 쭉~ 각각 상담을 해서 끝나는 날이라고 가정하고, 얼마를 벌 수 있는지를 보자.
    highest = 0
    for j in range(i-1, i-51, -1): # i보다 이른 날들을 보면서
        if j == 0:
            break
        if finish_days[j] <= n and get_moneys[j] > highest: # 상담 끝나는 날이 퇴사날보다 작아야 하고, highest보다 벌 수 있는 게 많으면
                highest = get_moneys[j]

    # 상담 안하고 다음날로 가는 경우
    if get_moneys[i] < get_moneys[i-1]:
        get_moneys[i] = get_moneys[i-1]

    # 컸을 때만 바꾸기
    if get_moneys[finish_days[i]] < (highest + prices[i]):
        get_moneys[finish_days[i]] = (highest + prices[i])

    # 그게 젤 많이 벌 수 있는 돈인지 체크하는 것
    if get_moneys[i] > res:
        res = get_moneys[i]

print(res)
