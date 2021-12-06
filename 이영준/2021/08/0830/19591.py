"""
Title : 독특한 계산기
Link : https://www.acmicpc.net/problem/19591
"""

import sys, collections
input = sys.stdin.readline


def calc(num1: int,  num2: int, cmd: str) -> int:
    if cmd == '+':
        return num1 + num2
    elif cmd == '-':
        return num1 - num2
    elif cmd == '*':
        return num1 * num2
    elif cmd == '/':
        return int(num1 / num2)


tmp = input().strip()
nums = collections.deque()
cmd = collections.deque()
# 식을 피연산자, 연산자 구분하여 리스트에 추가
st = 0
for i in range(1, len(tmp)):
    if tmp[i] in {'+', '-', '*', '/'}:
        nums.append(int(tmp[st:i]))
        cmd.append(tmp[i])
        st = i + 1
else:
    nums.append(int(tmp[st:]))

# 연산자 우선순위
priority = {'*': 2, '/': 2, '+': 1, '-': 1}

if len(nums) == 1:
    print(nums[0])
else:
    # 왼쪽 오른쪽이 한 연산자 기준 왼쪽, 오른쪽이면 종료
    # 아니면 우선순위에 따라 판별
    while len(nums) > 2:
        cmd1, cmd2 = cmd[0], cmd[-1]
        # 연산자 우선순위가 있는지
        p1, p2 = priority[cmd1], priority[cmd2]
        if p1 > p2:
            r = calc(nums[0], nums[1], cmd1)
            nums.popleft()
            nums.popleft()
            cmd.popleft()
            nums.appendleft(r)
        elif p1 < p2:
            r = calc(nums[-2], nums[-1], cmd2)
            nums.pop()
            nums.pop()
            cmd.pop()
            nums.append(r)
        # 연산자 우선순위가 같다면, 연산 값이 더 큰 것으로
        else:
            r1 = calc(nums[0], nums[1], cmd1)
            r2 = calc(nums[-2], nums[-1], cmd2)
            if r1 >= r2:
                nums.popleft()
                nums.popleft()
                cmd.popleft()
                nums.appendleft(r1)
            elif r1 < r2:
                nums.pop()
                nums.pop()
                cmd.pop()
                nums.append(r2)
    print(calc(*nums, cmd[0]))
