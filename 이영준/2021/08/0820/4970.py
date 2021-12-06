"""
Title : 디지털 회로 개론
Link : https://www.acmicpc.net/problem/4970
"""


def calc(poly: str) -> int:
    global p, q, r
    # 괄호 확인, 괄호 속 내용은 calc로 다시 계산
    # 괄호가 없다면, not, and, or 순서로 계산
    
    # 괄호 구간 시작을 찾는 인덱스
    st = -1
    # 다중 괄호 처리를 위해 여는, 닫는 괄호 개수 확인
    open, close = 0, 0
    # not이 여러번 나올때 개수 확인
    cnt_not = 0
    # 여러 값이 있을 때 앞의 값 저장
    value_before = -1
    # 직전 연산 저장
    cmd_before = ''
    for i in range(len(poly)):
        if poly[i] == '-':
            if open:
                continue
            cnt_not += 1
        elif poly[i] == '(':
            # 여는 괄호가 없으면 그 자리부터 시작
            if not open:
                st = i
            open += 1
        elif poly[i] == ')':
            close += 1
            # 여는 / 닫는 괄호 개수가 같으면 괄호 안 식 계산
            if open and open == close:
                value = calc(poly[st+1:i])
                # not 개수만큼 연산하고 저장
                for _ in range(cnt_not):
                    value = calc_not(value)
                # cnt_not 초기화
                cnt_not = 0
                # 직전 값이 없으면 저장
                # 직전 값이 있으면 연산자로 연산하여 저장
                if value_before == -1:
                    value_before = value
                else:
                    if cmd_before == '*':
                        value_before = calc_and(value_before, value)
                    elif cmd_before == '+':
                        value_before = calc_or(value_before, value)
                # 여는, 닫는 괄호 개수 초기화
                open, close = 0, 0
        elif poly[i] == '+' or poly[i] == '*':
            # 괄호 찾는 도중이면 넘어가기
            if open:
                continue
            # 다른 연산자를 만났을 때
            # 바로 앞에는 변수 or 상수가 있고
            # 사실상 모두 상수로 계산 가능
            # not 개수를 모두 사용해서 먼저 계산하고
            # 해당 연산값은 value_before에, 연산자는 cmd_before에 저장
            x = poly[i - 1]
            if x == ')':
                value = value_before
            elif x == 'P':
                value = p
            elif x == 'Q':
                value = q
            elif x == 'R':
                value = r
            else:
                value = int(x)
            for _ in range(cnt_not):
                value = calc_not(value)
            # cnt_not 초기화
            cnt_not = 0
            # 이전 저장된 값이 있는지
            if value_before == -1:
                value_before = value
            else:
                if cmd_before == '*':
                    value_before = calc_and(value_before, value)
                elif cmd_before == '+':
                    value_before = calc_or(value_before, value)
            cmd_before = poly[i]
    # 마지막 경우 두가지
    # 1. 마지막이 괄호로 끝나면 모든 계산이 완료됨 >> 해당 값으로 리턴
    if poly[-1] == ')':
        return value_before
    # 2. 마지막이 상수라면, 마지막 연산 한번 더 하고 리턴
    else:
        x = poly[-1]
        if x == 'P':
            value = p
        elif x == 'Q':
            value = q
        elif x == 'R':
            value = r
        else:
            value = int(x)
        # not 연산
        for _ in range(cnt_not):
            value = calc_not(value)
        if cmd_before == '*':
            return calc_and(value_before, value)
        elif cmd_before == '+':
            return calc_or(value_before, value)
        else:
            return value


def calc_not(x: int) -> int:
    if x == 0:
        return 2
    elif x == 1:
        return 1
    else:
        return 0


def calc_and(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0
    elif x == 2 and y == 2:
        return 2
    else:
        return 1


def calc_or(x: int, y: int) -> int:
    if x == 2 or y == 2:
        return 2
    elif x == 1 or y == 1:
        return 1
    else:
        return 0


while True:
    poly = input().strip()
    if poly == '.':
        break
    count = 0
    # 조합 확인
    # posible = []
    for p in range(3):
        for q in range(3):
            for r in range(3):
                if calc(poly) == 2:
                    count += 1
    #                 posible.append((p, q, r))
    # print(posible)
    print(count)
