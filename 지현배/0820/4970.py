import sys
input = sys.stdin.readline
# 시간이 많이 걸린 이유
# 1. 수많은 replace
# 2. 스택 전체 값을 건드림
while True:
    exp = input().rstrip()
    # 종료조건
    if exp == '.':
        break
    # 1. 반전 두번하면 원래 값이 나오므로 '--' 를 '-' 로 치환
    # 2. 두 개의 연산자를 비트 연산 '&', '|'로 취급
    # 3. 비트 연산을 위해 0, 1, 2를 각각 0b0, 0b1, 0b11로 취급
    # 4. 아래의 replace에서 위 숫자를 바꿔버리는 바람에 0, 1, 2가 들어가지 않는 2^n - 1 수로 지정
    # 5. 삼중 반복문에서 주어진 i, j, k 값에 따라 P, Q, R 값을 지정
    exp = exp\
    .replace('--', '').replace('*', '&').replace('+', '|')\
    .replace('-0', '63').replace('0', '3')\
    .replace('-1', '7').replace('1', '7')\
    .replace('-2', '3').replace('2', '63')\
    .replace('-P', '(3 if i == 2 else 7 if i == 1 else 63)')\
    .replace('-Q', '(3 if j == 2 else 7 if j == 1 else 63)')\
    .replace('-R', '(3 if k == 2 else 7 if k == 1 else 63)')\
    .replace('P', '(63 if i == 2 else 7 if i == 1 else 3)')\
    .replace('Q', '(63 if j == 2 else 7 if j == 1 else 3)')\
    .replace('R', '(63 if k == 2 else 7 if k == 1 else 3)')
    res = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                # 차례로 계산할 스택과 '('의 위치를 담을 스택
                stack = []
                open_idx = []
                for e in range(len(exp)):
                    # '('이면 계산 스택에서의 이 위치를 위치 스택에 담음
                    if exp[e] == '(':
                        open_idx.append(len(stack))
                    # 일단 스택에 담음
                    stack.append(exp[e])
                    # ')'이면 마지막 '('을 찾아 그 괄호 안을 계산함
                    if stack[-1] == ')':
                        idx = open_idx.pop()
                        temp = eval(''.join(stack[idx:]))
                        # 스택은 계산된 이전값만 남김
                        stack = stack[0:idx] 
                        # 스택에 값이 있으며 그 마지막이 '-'이면 계산 결과를 반전함
                        if len(stack) > 0 and stack[-1] == '-':
                            temp = 3 if temp == 63 else 7 if temp == 7 else 63
                            # '-'를 꺼냄
                            stack.pop()
                        # 계산결과를 문자열로 치환하여 다시 스택에 넣음
                        stack.append(str(temp))
                # 스택을 문자열로 바꾸어 값 비교함
                if ''.join(stack) == '63':
                    res += 1
    print(res)