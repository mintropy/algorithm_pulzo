"""
Title : PC방 요금
Link : https://www.acmicpc.net/problem/9080 
"""

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    st_time, duration = input().strip().split()
    # 시간 시간, 분
    st_h, st_m = map(int, st_time.split(':'))
    # 시간을 00:00 기준 지난 시간
    now = st_h * 60 + st_m
    # 총 사용 시간
    duration = int(duration)
    
    fee = 0
    while duration:
        # 만약 남은 시간이 5시간 이하면 시간별 요금 내기
        if duration <= 60 * 5:
            if duration % 60:
                fee += (duration // 60 + 1) * 1000
            else: 
                fee += (duration // 60) * 1000
            break
        # 제한시간이 더 많이 남아있을 때
        # 야간이고 남은 시간이 5시간 이상이면 정액제
        if now >= 22 * 60 or now <= 3 * 60:
            # 08:00 기준에서 지금시간까지 빼기
            if now >= 22 * 60:
                duration -= (24 + 8) * 60 - now
            else:
                duration -= 8 * 60 - now
            fee += 5000
            now = 8 * 60
        # 야간 남은 시간 5시간 미만이거나, 주간이면
        # 21:~~ 까지 사용하기
        elif 3 * 60 < now < 21 * 60:
            time = 21 - now // 60
            # 더 사용할 시간이 적으면, 모두 사용
            if time * 60 >= duration:
                if duration % 60:
                    fee += (duration // 60 + 1) * 1000
                else: 
                    fee += (duration // 60) * 1000
                break
            # time에 해당하는 시간만큼만 사용
            else:
                fee += time * 1000
                duration -= time * 60
                now += time * 60
        # 21:~~ 이라면 어떻게 할 지 고민하기
        else:
            # 21:00 이면 한시간 진행
            if now == 21 * 60:
                if duration > 60:
                    now += 60
                    fee += 1000
                    duration -= 60
                    continue
                else:
                    fee += 1000
                    break
            time = 10 * 60 + (22 * 60 - now)
            # 다음날 08:00 이후까지 하는 경우
            if duration >= time:
                now = 8 * 60
                fee += 1000 + 5000
                duration -= time
            # 야간 5시간 이상 하는 경우
            elif duration - (22 * 60 - now) >= 60 * 5:
                fee += 1000 + 5000
                break
            # 야간 5시간 미만 하는 경우
            else:
                if duration % 60:
                    fee += (duration // 60 + 1) * 1000
                else: 
                    fee += (duration // 60) * 1000
                break
    print(fee)


'''
Counter Example
1
08:30 4316
ans : 58000

1
03:00 720
ans : 

'''

'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    st_time, duration = input().strip().split()
    # 시간 시간, 분
    st_h, st_m = map(int, st_time.split(':'))
    # 총 사용 시간
    duration = int(duration)
    
    fee = 0
    while duration:
        # 야간 시간
        if st_h == 22 and st_m == 0:
            # 남은 시간이 5시간 이상일 때와 아닐때로
            if duration >= 60 * 5:
                fee += 5000
                if duration >= 60 * 10:
                    st_h = 8
                    duration -= 60 * 10
                else:
                    break
            else:
                if duration % 60:
                    duration //= 60
                    duration += 1
                else:
                    duration //= 60
                fee += duration * 1000
                break
        # 주간 시작
        elif st_h == 8 and st_m == 0:
            # 전체 남은 사용 시간이 5시간 이하인 경우
            if duration <= 60 * 5:
                if duration % 60:
                    duration //= 60
                    duration += 1
                else:
                    duration //= 60
                fee += duration * 1000
                break
            # 주간을 풀로 채울 수 있을 때
            if duration >= 14 * 60:
                fee += 14 * 1000
                st_h = 22
                duration -= 14 * 60
            else:
                if duration % 60:
                    duration //= 60
                    duration += 1
                else:
                    duration //= 60
                fee += duration * 1000
                break
        # 주간
        elif 8 <= st_h < 22:
            # 전체 남은 사용 시간이 5시간 이하인 경우
            if duration <= 60 * 5:
                if duration % 60:
                    duration //= 60
                    duration += 1
                else:
                    duration //= 60
                fee += duration * 1000
                break
            # 야간 시작 까지 남은 시간
            left_time = (21 - st_h) * 60 + (60 - st_m)
            if duration >= left_time:
                if left_time % 60:
                    fee += ((left_time // 60) + 1) * 1000
                else:
                    fee += (left_time // 60) * 1000
                st_h = 22
                st_m = 0
                duration -= left_time
            else:
                if duration % 60:
                    duration //= 60
                    duration += 1
                else:
                    duration //= 60
                fee += duration * 1000
                break
        # 야간
        else:
            # 주간 시간 까지 남은 시간
            if st_h >= 22:
                left_time = 60 * 8 + (23 - st_h) * 60 + (60 - st_m)
            else:
                left_time = (7 - st_h) * 60 + (60 - st_m)
            # 남은 시간이 5시간 이상일 때와 아닐때로
            if duration >= 60 * 5 and left_time >= 60 * 5:
                fee += 5000
                if duration - left_time >= 0:
                    st_h = 8
                    st_m = 0
                    duration -= left_time
                else:
                    break
            else:
                if left_time >= duration:
                    if duration % 60:
                        duration //= 60
                        duration += 1
                    else:
                        duration //= 60
                    fee += duration * 1000
                    break
                else:
                    if left_time % 60:
                        left_time //= 60
                        left_time += 1
                    else:
                        left_time //= 60
                    fee += left_time * 1000
                    break
    print(fee)
'''
