def solution(fees, records):
    # 각 차량번호를 키, 값으로 총 주차시간, 출입 시간 저장
    # 만약 출입이면 출입시간에 저장
    # 퇴장이면 출입시간과 비교하여 총 주차시간 계산
    # 퇴장 후 다시 ''으로 변경
    parking_info = {}
    for record in records:
        # 시간, 차량번호, 입출입
        time, num, how = record.split()
        if how == 'IN':
            if num in parking_info:
                parking_info[num][1] = time
            else:
                parking_info[num] = [0, time]
        else:
            st_time = parking_info[num][1].split(':')
            time = time.split(':')
            # 시간별 분별 계산 보다, 00:00 기준 몇 분 후인지로 계산
            st = int(st_time[0]) * 60 + int(st_time[1])
            end = int(time[0]) * 60 + int(time[1])
            parking_time = end - st
            # 정보 갱신
            parking_info[num][0] += parking_time
            parking_info[num][1] = ''
    
    # 추가적으로 나가지 않은 차량에 대하여 확인
    # 나가지 않은 차량에 대한 출차 기준 시간은 동일
    end = 23 * 60 + 59
    for num in parking_info:
        if parking_info[num][1]:
            st_time = parking_info[num][1].split(':')
            st = int(st_time[0]) * 60 + int(st_time[1])
            parking_info[num][0] += end - st
    
    answer = []
    for num in sorted(parking_info.keys()):
        total_parking_time = parking_info[num][0]
        # 기본 요금 시간보다 적은지
        if total_parking_time <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1]
            total_parking_time -= fees[0]
            if total_parking_time % fees[2]:
                fee += (total_parking_time // fees[2] + 1) * fees[3]
            else:
                fee += (total_parking_time // fees[2]) * fees[3]
            answer.append(fee)
    return answer