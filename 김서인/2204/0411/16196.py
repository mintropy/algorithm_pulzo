import sys

input = sys.stdin.readline

n = input().rstrip()
N = int(input())
area_codes = [input().rstrip() for _ in range(N)]


def sol():
    # 지역 코드 체크
    if n[:6] not in area_codes:
        return 'I'

    # 생일 코드 체크 (1900.01.01-2011.12.31 & 윤년 체크)
    year = n[6:10]
    month = n[10:12]
    date = n[12:14]

    if 1900 <= int(year) <= 2011:
        pass
    else:
        return 'I'

    if 1 <= int(month) <= 12:
        pass
    else:
        return 'I'

    # 30일까지 있는 달
    if month == '04' or month == '06' or month == '09' or month == '11':
        if 1 <= int(date) <= 30:
            pass
        else:
            return 'I'

    # 31일까지 있는 달
    if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
        if 1 <= int(date) <= 31:
            pass
        else:
            return 'I'

    # 2월
    if month == '02':
        tmp_year = int(year)

        if tmp_year % 400 == 0:  # 윤년
            if 1 <= int(date) <= 29:
                pass
            else:
                return 'I'
        elif tmp_year % 100 == 0:  # 평년
            if 1 <= int(date) <= 28:
                pass
            else:
                return 'I'

        elif tmp_year % 4 == 0:  # 윤년
            if 1 <= int(date) <= 29:
                pass
            else:
                return 'I'
        else:  # 평년
            if 1 <= int(date) <= 28:
                pass
            else:
                return 'I'

    # 체크섬 코드 계산(x는 0~10. 10이면 X)
    check_sum = n[17]
    if check_sum == 'X':
        check_sum_tmp = 10
    else:
        check_sum_tmp = int(check_sum)

    for i in range(17):
        check_sum_tmp += (int(n[i])) * (2 ** (17 - i))
        check_sum_tmp %= 11

    if (check_sum_tmp) % 11 == 1:
        # 순서 코드 체크
        if n[14:17] == '000':
            return 'I'
        elif int(n[14:17]) % 2:  # 남
            return 'M'
        else:  # 여
            return 'F'
    else:
        return 'I'


print(sol())
