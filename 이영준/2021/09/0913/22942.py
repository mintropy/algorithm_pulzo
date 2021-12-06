"""
Title : 데이터 체커
Link : https://www.acmicpc.net/problem/22942
"""

import sys
input = sys.stdin.readline

n = int(input())
circles = sorted(list(tuple(map(int, input().split())) for _ in range(n)))

stack = []

for center, radius in circles:
    if not stack:
        stack.append((center, radius))
    # 이전 저장된 원의 외부에 있으면 append
    # 확인하는 원이 이전원의 내부라면 continue
    # 이전 저장된 원이 내부라면, 외부에 있는 원이 나올때 까지 stack에서 pop
    else:
        is_valid = True
        todo = False
        while stack:
            dist = center - stack[-1][0]
            # 이전원과 겹칠 때
            if abs(radius - stack[-1][1]) <= dist <= radius + stack[-1][1]:
                is_valid = False
                break
            # 이전 원의 외부일 때
            if dist > radius + stack[-1][1]:
                stack.append((center, radius))
                break
            # 지금 원이 이전 원의 내부일 때
            elif dist < stack[-1][1]:
                break
            # 이전 원이 지금 원의 내부일 때
            elif dist + stack[-1][1] < radius:
                stack.pop()
        if not is_valid:
            print('NO')
            break
        if not stack:
            stack.append((center, radius))
else:
    print('YES')
