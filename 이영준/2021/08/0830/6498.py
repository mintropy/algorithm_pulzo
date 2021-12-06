"""
Title : 엘리어스 감마 코드
Link : https://www.acmicpc.net/problem/6498
"""

# https://www.informatik.uni-ulm.de/acm/Locals/2009/html/judge.html

import sys
input = sys.stdin.readline


while True:
    n = int(input())
    if n == 0:
        break
    count = [0] + list(map(int, input().split()))
    prefix_sum = count[::]
    for i in range(1, n + 1):
        prefix_sum[i] += prefix_sum[i - 1]
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # prefix 1개일 때
    for j in range(1, n + 1):
        bits = prefix_sum[j]
        dp[1][j] = (1 + j) * bits
    
    # prefix 개수
    for i in range(2, n + 1):
        # 보고있는 마지막 비트 길이
        for j in range(i, n + 1):
            tmp = []
            # 참조할 이전 칸
            # k비트 길이부터 j비트 길이까지 확인
            for k in range(j - i + 1):
                # 해당 범위의 비트 개수
                bits = prefix_sum[j] - prefix_sum[j - k - 1]
                tmp.append(dp[i - 1][j - 1 - k] + (i + j) * bits)
            dp[i][j] = min(tmp)
            
    
    min_bits = dp[1][n]
    for i in range(2, n + 1):
        if min_bits > dp[i][n]:
            min_bits = dp[i][n]
    print(min_bits)


'''
while True:
    n = int(input())
    if n == 0:
        break
    count = [0] + list(map(int, input().split()))
    # 누적합으로 구현
    for i in range(n - 1, 0, -1):
        count[i] += count[i + 1]
    
    # prefix의 0개수, 2조건에 따라 0 추가했는지
    gamma = {i: [i - 1, 0] for i in range(n + 1)}
    
    # 감마 코드 축약
    for i in range(1, n):
        # 해당 길이 감마 코드 없으면 0 하나씩 축약
        # 해당 길이 감마 코드 개수
        c = count[i] - count[i + 1]
        if c == 0:
            for j in range(i + 1, n + 1):
                gamma[j][0] -= 1
        # 아니라면 2번 방법 가능한지 확인
        else:
            c_next = count[i + 1]
            # 더 긴 길이 이상의 수열이 더 많을 때 시행
            if c_next > c:
                # 같은 길이 prefix중, 이미 시행했으면 넘어가기
                # 하나만 앞으로 확인하면 됨
                if gamma[i - 1][0] == gamma[i][0] and gamma[i - 1][1]:
                    continue
                else:
                    gamma[i][1] = 1
                    for j in range(i + 1, n + 1):
                        gamma[j][0] -= 1
    else:
        # 마지막 자리 확인
        # prefix가 다를 때
        if gamma[n][0] != gamma[n - 1][0]:
            if gamma[n - 1][1]:
                gamma[n][0] -= 1
    
    # 사용한 비트 수 확인
    total_bit = 0
    for i in range(1, n + 1):
        # 해당 길이 수 개수
        if i == n:
            seq_count = count[i]
        else:
            seq_count = count[i] - count[i + 1]
        # prefix 길이
        add_bit = sum(gamma[i])
        total_bit += (i + add_bit + 1) * seq_count
    
    print(total_bit)
'''