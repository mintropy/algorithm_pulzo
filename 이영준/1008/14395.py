"""
Title : 4연산
Link : https://www.acmicpc.net/problem/14395
"""

import collections


def bfs(s: int, t: int) -> str:
    # 4연산 실행
    if s == t:
        return 0
    # -는 사용할 필요 없음 / 0 안나옴
    # /도 처음에만 사용하면 됨
    queue = collections.deque([(s, ''), (1, '/')])
    prob_operation = []
    while queue:
        num, operation = queue.popleft()
        if num == t:
            prob_operation.append(operation)
            continue
        # +, * 진행
        if num + num <= t:
            queue.append((num + num, operation + '+'))
        if num * num <= t and num != 1 :
            queue.append((num * num, operation + '*'))
    if prob_operation:
        prob_operation.sort(key=lambda x:(len(x), x))
        return prob_operation[0]
    else:
        return -1


s, t = map(int, input().split())
print(bfs(s, t))
