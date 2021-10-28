import collections
import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, T, W = MIIS()

bank_line = collections.deque()  # 은행 대기 줄

# 영업 시작할 때 대기 줄에 이미 있는 손님
for _ in range(N):
    p, t = MIIS()
    bank_line.append((p, t))

# 오픈 후에 오는 손님
M = int(input())
after_customers = list()
for _ in range(M):
    p, t, c = MIIS()
    after_customers.append((c, p, t))
after_customers.sort()
after_customers = collections.deque(after_customers)

now = 0
while bank_line and now < W:
    # 맨 앞의 고객 만나기
    curr_customer_p, curr_customer_t = bank_line.popleft()

    if curr_customer_t >= T:  # 고객이 필요한 시간이 T보다 크거나 같으면
        i = 0
        while i < T and now < W:  # T 초 동안 그 고객을 만나기
            print(curr_customer_p)
            now += 1
            i += 1

            # 이 시각 이전에 은행에 들어온 고객이 있으면 줄 서게 하기
            while after_customers and now == after_customers[0][0]:
                tmp_c, tmp_p, tmp_t = after_customers.popleft()
                bank_line.append((tmp_p, tmp_t))

        if curr_customer_t > T:  # 고객이 다시 뒤에 가서 서야 하면
            bank_line.append((curr_customer_p, curr_customer_t - T))  # 다시 맨 뒤에 서세요.



    elif curr_customer_t < T:  # 고객이 필요한 시간이 T시간보다 작으면
        i = 0
        while i < curr_customer_t and now < W:
            print(curr_customer_p)  # 고객이 필요한 시간만큼 그 고객 만나기
            now += 1
            i += 1

            # 이 시각 이전에 은행에 들어온 고객이 있으면 줄 서게 하기
            while after_customers and now == after_customers[0][0]:
                tmp_c, tmp_p, tmp_t = after_customers.popleft()
                bank_line.append((tmp_p, tmp_t))
