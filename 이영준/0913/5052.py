"""
Title : 전화번호 목록
Link : https://www.acmicpc.net/problem/5052
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    # 각 점에 대하여 점을 키, 자식을 값으로 저장하는 딕셔너리
    # 각 점이 번호의 끝일때 True로 저장
    num_tree = {'-1': [False, set()]}
    
    # 다른 번호의 접두어가 되는 번호가 있는지
    prefix_exist = False
    for __ in range(n):
        phone_number = tuple(input().strip())
        if prefix_exist:
            continue
        for i in range(len(phone_number)):
            prefix = ''.join(phone_number[:i])
            now = prefix + phone_number[i]
            # 접두어는 이미 등록되어 있으므로, 각 값의 첫 번째가 True인지 확인
            if i != 0 and num_tree[prefix][0]:
                prefix_exist = True
                break
            # 탐색
            if i == 0:
                if now in num_tree['-1'][1]:
                    continue
                else:
                    num_tree['-1'][1].add(now)
                    num_tree[now] = [False, set()]
            else:
                if now in num_tree[prefix][1]:
                    continue
                else:
                    num_tree[prefix][1].add(now)
                    num_tree[now] = [False, set()]
        # 마지막 전체 번호 확인
        else:
            # now는 이정에 저장한 것 그대로 사용 가능
            if num_tree[now][1]:
                prefix_exist = True
            else:
                num_tree[now][0] = True
    
    if prefix_exist:
        print('NO')
    else:
        print('YES')



'''
2
3
91125426
911
97625999
5
113
12340
123440
12345
98346
'''
