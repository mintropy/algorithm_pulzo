def solution(fees, records):
    answer = []
    DT, DC, UT, UC = fees
    # 주차장 현재 상황
    status = dict()
    # 차 번호별 시간 합
    toTime = dict()
    for record in records:
        time, number, history = record.split()
        if history == 'IN':
            status[number] = time
        else:
            # 나간시간, 들어온시간 차를 구해서 toTime에 더한다.
            ph, pm = map(int, status[number].split(':'))
            ch, cm = map(int, time.split(':'))
            ctime = (ch - ph) * 60 + cm - pm
            if toTime[number]:
                toTime[number] += ctime
            else:
                toTime[number] = ctime
            # 빠져 나갔음을 표시
            status[number] = ''
    # 아직 안나간 차들 23:59에 나간거로 취급
    for k, v in status.items():
        if v:
            ph, pm = map(int, status[k].split(':'))
            ctime = (23 - ph) * 60 + 59 - pm
            if toTime[k]:
                toTime[k] += ctime
            else:
                toTime[k] = ctime
            status[k] = ''
    # 누적된 시간만큼 요금 구함
    for k, v in toTime.items():
        totalTime = v - DT
        if totalTime <= 0: answer.append([k, DC])
        else: answer.append([k + DC + int(totalTime / UT + 0.5) * UC])
    return map(lambda x: int(x[1]), answer.sort())