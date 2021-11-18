import collections
import sys

input = sys.stdin.readline

N = int(input())
mos_time = list(tuple(map(int, input().split())) for _ in range(N))
mos_time.sort()
# mos_check = [0]*(2100000001)
mos_check = collections.defaultdict(int)

max_time = 0
# 모기 출입 시간 체크
for i in range(N):
    check_in, check_out = mos_time[i]
    mos_check[check_in] += 1
    mos_check[check_out] -= 1
    # max_time = max(max_time, check_out)

max_time = max(mos_check.keys())
# 가장 많이 있는 시간대, 그때 몇 마리인지
mos_hot_time = [0, 0]
# mos_cnt = [0] * (max_time + 1)
curr_mos_cnt, next_mos_cnt = 0, 0
max_mos_cnt = 0
max_first_flag = False
# 모기가 등장할 때만 확인.
mos = list(mos_check.keys())
mos.sort()
for i in mos:
    next_mos_cnt = curr_mos_cnt + mos_check[i]
    if next_mos_cnt > max_mos_cnt:
        max_mos_cnt = next_mos_cnt
        mos_hot_time[0] = i  # 시작 시간
        max_first_flag = True
    elif next_mos_cnt == max_mos_cnt and max_first_flag == True:
        mos_hot_time[1] = i  # 끝시간 매번 갱신
    elif next_mos_cnt < max_mos_cnt and max_first_flag==True:
        mos_hot_time[1] = i
        max_first_flag = False
    curr_mos_cnt = next_mos_cnt

print(max_mos_cnt)
start = mos_hot_time[0]
end = mos_hot_time[1]
print(start, end)

