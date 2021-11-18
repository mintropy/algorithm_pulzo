# 가격이 같은 고기가 여러 개 있는 경우를 고려하기..! (가격 같은 것 여러 개 구매 VS 가격 하나 더 비싼 고기 하나 구매)
# 시간 초과 -> dp 만들어서 시간 초과는 괜찮아짐 -> 그런데 9%에서 틀림..ㅠㅠ 

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
meats = []

for _ in range(N):
    meats.append(tuple(map(int,input().split())))

meats.sort(key=lambda x:(x[1],-x[0]))  # 가격 기준으로 싼 것부터 정렬 -> 가격 같으면 무게 큰 걸 먼저 정렬

dp = [0] * N # 해당 덩어리를 구매하면, 고기 양 얼마나 얻는지 

min_price = 2147483648
cnt = 1  # 가격 같은 것 여러 개 구매해야 할 때, 몇 개 구매해야 하는지 그 갯수

for i in range(len(meats)): # 가격 기준으로 쭉 돌아보기(싼 것부터)
    # 그 가격 이하의 고기 양 합이 필요한 양보다 많은지
    price = meats[i][1]
    
    if i != 0 and price == meats[i-1][1]:  # 가격 같은 것 여러 개 구매하는 경우
        cnt += 1
    else:
        cnt = 1

    dp[i] = dp[i-1] + meats[i][0]
    
    if dp[i] >= M:
        if price == meats[i-1][1]: # 가격 같은 것 여러 개 구매하는 경우
            min_price = min(price*cnt, min_price)

        else:  # 하나 구매하는 경우
            min_price = min(price, min_price)


if min_price == 2147483648: # 불가능한 경우
    print(-1)
else:
    print(min_price)

# print(meats)
# print(dp)

"""
input1
3 2
1 5
1 5
2 6

ans1
6

input2
10 10
2 3
2 4
2 5
3 1
1 3
7 9
7 3
8 4
10 3
3 10

ans2
 3

input3
4 3
1 2
3 2
2 2
5 7
ans3 
2

input4
2 100
1 2
1 2

output 4
-1


input5
2 100
99 2
1 2

output 5
4

input6
5 150
50 3
50 3
50 3
75 5
75 5

output6
5

input7
4 10
1 2
1 2
4 4
4 4


"""