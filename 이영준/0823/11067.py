"""
Title : 모노톤길
Link : https://www.acmicpc.net/problem/11067
"""

import sys, collections
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    cafe = collections.defaultdict(list)
    for _ in range(n):
        x, y = map(int, input().split())
        cafe[x].append(y)
    m_q = list(map(int, input().split()))
    query = m_q[1:]
    
    cafe_now = 0
    cafe_count = {}
    now = [-1, 0]
    
    # 카페 순서대로 탐색
    # x좌표가 다르면 x좌표를 전진
    # 전지 시킬 때, 같은 y좌표가 가장 큰지 작은지 확인
    # >> 가장 작고, 크고에 따라 진행방향의 위, 아래 결정됨
    # 나머지 카페들은 순서대로 개수 확인
    for x in sorted(cafe.keys()):
        pos = sorted(cafe[x])
        # 이전 y좌표가 가장 작을 때
        if now[1] == pos[0]:
            # 나머지 모든 좌표 순서대로 확인
            for i in range(len(pos)):
                cafe_now += 1
                cafe_count[cafe_now] = (x, pos[i])
            now = [x, pos[-1]]
        # 이전 y좌표가 가장 클 때
        else:
            # 나머지 모든 좌표 순서대로 확인
            for i in range(len(pos) - 1, -1, -1):
                cafe_now += 1
                cafe_count[cafe_now] = (x, pos[i])
            now = [x, pos[0]]
    
    # 쿼리 순서대로 출력
    for q in query:
        print(*cafe_count[q])



'''
1
11
0 0
0 1
0 2
0 3
2 4
2 5
2 3
5 0
5 5
8 0
8 8
5 2 4 6 8 10
'''