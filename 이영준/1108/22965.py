"""
Title : k개의 부분 배열
Link : https://www.acmicpc.net/problem/22965
"""

import sys
input = sys.stdin.readline


N = int(input())
seq = list(map(int, input().split()))

count_piece = 1
for i in range(N - 1):
    # 증가하는 부분이면 확인 ㄴㄴ
    # 감소하는 부분 만나면 적어도 2조각 필요
    if seq[i] > seq[i + 1]:
        count_piece += 1
    # 지금 두번 째 조각인데, 앞의 조각 사이에 넣어야 할 때
    if count_piece == 2 and seq[i + 1] > seq[0]:
        count_piece += 1
    # 무조건 3조각이면 가능
    if count_piece == 3:
        break

print(count_piece)


'''
Counter Example
6
5 3 1 2 4 6
ans : 3

6
1 5 9 2 3 4
ans : 3

6
1 3 5 6 4 2
ans : 3
'''