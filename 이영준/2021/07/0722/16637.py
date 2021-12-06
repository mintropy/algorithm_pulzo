'''
Title : 괄호 추가하기
Link : https://www.acmicpc.net/problem/16637
'''

import sys, itertools

input = sys.stdin.readline

def calc(nums: list, operators: list) -> int:
    """
    주어진 숫자 nums와 연산자 operators의 연산 결과 반환
    """
    result = nums[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += nums[i + 1]
        elif operators[i] == '-':
            result -= nums[i + 1]
        elif operators[i] == '*':
            result *= nums[i + 1]
    return result

def is_possible(op: list) -> bool:
    """
    괄호를 쳐서 먼저 연산하게 될 연산자를 뽑았을 때, 가능한지 판별
    """
    if type(op) == int:
        return True
    else:
        for i in range(len(op) - 1):
            if op[i + 1] - op[i] == 1:
                return False
        return True

def contraction(nums, operators, operator):
    """
    뽑을 연산자 위치 operator를 받아서,
    각 위치 연산자를 우선적으로(괄호 연산)을 한 식을 반환
    """
    num_to_calc = []
    operators_to_calc = []
    idx = 0
    prev_idx = -1
    if type(operator) == int:
        operator = (operator,)
    for i in range(len(operators)):
        if i == operator[idx]:
            if operators[operator[idx]] == '+':
                c = nums[i] + nums[i + 1]
            elif operators[operator[idx]] == '-':
                c = nums[i] - nums[i + 1]
            elif operators[operator[idx]] == '*':
                c = nums[i] * nums[i + 1]
            num_to_calc.append(c)
            prev_idx = idx
            if idx == len(operator) - 1:
                continue
            else:
                idx += 1
        elif i == operator[prev_idx] + 1:
            operators_to_calc.append(operators[i])
        else:
            num_to_calc.append(nums[i])
            operators_to_calc.append(operators[i])
    # nums의 마지막 숫자가 계산되지 않은 경우 따로 추가
    # 연산할 위치 operator의 마지막 idx를 확인
    num_to_calc.append(nums[-1])
    return num_to_calc, operators_to_calc


n = int(input())
equation = str(input().strip())
nums = []
operators = []
# 주어진 식을 문자열로 받아, 숫자, 연산자로 구분
for i in range(n):
    if i % 2 == 0:
        nums.append(int(equation[i]))
    elif i % 2 == 1:
        operators.append(equation[i])

# 최대값 저장
max_result = -1 * (2 ** 31)

# 괄호를 칠 수 있는 최대 개수
if len(operators) % 2 == 0:
    max_bracket = len(operators) // 2
else:
    max_bracket = len(operators) // 2 + 1

# 괄호 개수별로 계산 실행
for i in range(max_bracket + 1):
    # 괄호가 없을 때
    if i == 0:
        result = calc(nums, operators)
        if result > max_result:
            max_result = result
        continue
    # 괄호 하나일 때
    elif i == 1:
        permutation_of_operators = list(range(len(operators)))
    else:
        permutation_of_operators = list(itertools.combinations(range(len(operators)), i))
    for operator in permutation_of_operators:
        # 괄호 위치가 가능한지 확인
        if is_possible(operator):
            # 괄호 위치 operator를 확인하여, 괄호 우선 연산된 결과 확인
            num_to_calc, operators_to_calc = contraction(nums, operators, operator)
            # 위의 연산 결과 식을 앞에서부터 연산 실행
            result = calc(num_to_calc, operators_to_calc)
            if result > max_result:
                max_result = result

print(max_result)       
