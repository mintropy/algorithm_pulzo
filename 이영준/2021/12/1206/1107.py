'''
Title : 리모컨
Link : https://www.acmicpc.net/problem/1107
'''

import sys
input = sys.stdin.readline


def check_possible(num: int, possible_nums: list) -> bool:
    if num == 0:
        if 0 in possible_nums:
            return True
        else:
            return False
    while num:
        num, m = divmod(num, 10)
        if m not in possible_nums:
            return False
    return True


target_channel_num = int(input())
broken_num_count = int(input())
broken_nums = set(map(int, input().split()))
possible_nums = set(range(10)) - broken_nums

min_button = abs(100 - target_channel_num)
for st_num in range(target_channel_num, -1, -1):
    btn = target_channel_num - st_num
    if btn > min_button:
        break
    if not check_possible(st_num, possible_nums):
        continue
    if btn + len(str(st_num)) < min_button:
        min_button = btn + len(str(st_num))
for st_num in range(target_channel_num, 1_000_001):
    btn = st_num - target_channel_num
    if btn > min_button:
        break
    if not check_possible(st_num, possible_nums):
        continue
    if btn + len(str(st_num)) < min_button:
        min_button = btn + len(str(st_num))

print(min_button)


'''
def plus_to_channel(m, alive):
    global channel
    count = 0
    if len(channel) == 1:
        want = int(channel[0])
        if alive[0] > want:
            return int(1e6)
        else:
            min_of_max = alive[0]
            for button in alive:
                if button <= want:
                    min_of_max = button
            return want - button
    else:
        channel_num = int(''.join(channel))
        # 같은 자리수 중 더 작은값이 있는지
        if alive[0] == 0:
            min_button_none_zero = alive[1]
        else:
            min_button_none_zero = alive[0]
        # 채널과 같은 자리수로 만들 수 있는지
        if min_button_none_zero <= int(channel[0]):
            # 같은 자리수 일 때
            new_channel_length = len(channel)
            new_channel = 0
            # 코드 추가하기
            pass

        else:
            # 하나 짧은 자리수일 때
            new_channel_length = len(channel) - 1
            new_channel = alive[-1]
            for _ in range(new_channel_length - 1):
                new_channel *= 10
                new_channel += alive[-1]
            return channel_num - new_channel
    


channel = list(input().strip())
m = int(input())
broken = list(map(int, input().split()))
alive = list(range(0, 10))
alive = list(set(alive) - set(broken))

# 100번부터 +, - 버튼만으로 이동
count_only_plus_minus = abs(channel - 100)
if m == 10:
    print(count_only_plus_minus)
else:
    # 숫자버튼으로 이동 후, +, - 버튼으로 이동하는 회수
    count_num_plus = plus_to_channel(m, broken)
'''

'''
Counter Example
0
0

ans : 1

2
9
0 1 2 3 4 5 6 7 8

'''