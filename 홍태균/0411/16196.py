'''
중국 신분증 번호

'''
import sys
input = sys.stdin.readline

code = input().strip()

n = int(input())
# 지역 코드 리스트
loc_codes = [input().strip() for _ in range(n)]
# 지역코드
loc_code = code[:6]
# 생일코드
bir_code = code[6:14]
# 순서코드
ord_code = code[14:17]
# 날짜
m_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def check():
    # 지역 코드 오류
    if loc_code not in loc_codes:
        return 'I'
    
    # 생일 코드 확인
    Y = int(bir_code[:4])
    M = int(bir_code[4:6])
    D = int(bir_code[6:8])
    # 년도
    if 1900 <= Y <= 2011:
        yun = 0
        # 월
        if 1 <= M <= 12:
            # 윤년 계산
            if M == 2:
                if Y % 4 == 0:
                    if Y % 100 == 0:
                        if Y % 400 == 0:
                            yun = 1
                        else:
                            yun = 0
                    else:
                        yun = 1
            # 일            
            if 1<= D <= m_day[M] + yun:
                pass
            else:
                return 'I'
        else:
            return 'I'
    else:
        return 'I'
    
    # 순서 코드 오류
    if ord_code == '000':
        return 'I'
    
    # 체크섬 확인
    sum_code = 0

    for i in range(17):
        sum_code += (int(code[i]) * (2**(17-i))) % 11
        
    if code[-1] == 'X':
        check_sum = 10
    else:
        check_sum = int(code[-1])
    
    # 다 맞다면 성별 출력
    if (sum_code + check_sum) % 11 == 1:
        if int(ord_code) % 2:
            return 'M'
        else:
            return 'F'
    # 체크섬 오류
    else:
        return 'I'
            
print(check())        
        
        