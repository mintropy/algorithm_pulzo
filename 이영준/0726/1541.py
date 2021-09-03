"""
Title : 읽어버린 괄호
Link : https://www.acmicpc.net/problem/1541
"""

import sys

input = sys.stdin.readline

def make_bracket(eq):
    new_eq = []
    for e in eq:
        # -기호를 기준으로 분해된 식에서 숫자만 추출
        # 0으로 시작하는 숫자가 존재하기 때문에 int로 변환
        # 숫자의 합을 str로 저장
        nums = list(map(int, e.split('+')))
        new_eq.append(str(sum(nums)))
    # 각 구분된 식의 값을 -기호를 추가한 상태로 문자열로 반환
    return '-'.join(new_eq)

# -기호를 기준으로 분해
eq = list(map(str, input().strip().split('-')))
new_eq = make_bracket(eq)
print(eval(new_eq))


'''
# 실패코드
# 1. 최솟값이 아닌 최댓값으로 만듬
# 2. 모든 숫자 위치를 확인할 필요가 없음
def make_bracket(eq):
    new_eq = ''
    # 초기 값 idx, num1_st, num1_end설정
    idx = 0
    num1_st = 0
    for i in range(1, 6):
        try:
            int(eq[idx + i])
        except:
            num1_end = i
            idx += i + 1
            break
    operator = idx - 1
    tmp_eq = ''
    
    while idx < len(eq):
        num2_st = idx
        for i in range(1, 6):
            if idx + i == len(eq):
                num2_end = idx + i
                idx += i
                break
            try:
                int(eq[idx + i])
            except:
                num2_end = idx + i
                idx += i + 1
                break
        # 연산자 앞뒤로 숫자 확인
        # 연산자가 +일 때, num1을 tmp_eq에 추가
        # tmp_eq를 괄호를 쳐서 new_eq에 추가
        # new_eq에 연산자 추가
        # 연산자가 -일 때, num1과 연산자를 tmp_eq에 추가
        tmp_eq += eq[num1_st:num1_end]
        if eq[operator] == '+':
            new_eq += '(' + tmp_eq + ')'
            tmp_eq = ''
            new_eq += eq[operator]
        elif eq[operator] == '-':
            tmp_eq += eq[operator]
        # num2를 num1으로 교체
        # 연산자 위치를 num1다음 인덱스로 변경
        num1_st, num1_end = num2_st, num2_end
        operator = idx - 1
    # 마지막 남은 num2를 tmp_eq에 추가하여 new_eq에 추가
    tmp_eq += eq[num2_st:num2_end]
    new_eq += tmp_eq
    return new_eq

eq = str(input().strip())
new_eq = make_bracket(eq)
print(eval(new_eq))
'''

