'''
도서관

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

num_list = list(map(int,input().split()))

# 양수와 음수를 나누어서 저장
plus_list = []
minus_list = []

for i in num_list:
    if i > 0:
        plus_list.append(i)
    else:
        minus_list.append(i)

# 정렬
plus_list.sort(key=lambda x:-x)
minus_list.sort()


total = 0
# 뛰어넘으면서 * 2를 해서 저장
for i in range(0,len(plus_list),M):
    total += plus_list[i] * 2
for i in range(0,len(minus_list),M):
    total += (-minus_list[i]) * 2

# 양수와 음수가 둘다 있다면
# 절댓값이 큰 곳은 1번만 왔다갔다하게
if plus_list and minus_list:
    if plus_list[0] > -minus_list[0]:
        total -= plus_list[0]
    else:
        total += minus_list[0]
# 만약 1쪽만 있을 경우 한쪽의 가장 큰 값을 1번만 왔다갔다
elif plus_list:
    total -= plus_list[0]
else:
    total += minus_list[0]

print(total)