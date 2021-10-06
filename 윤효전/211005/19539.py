import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
S = list(map(int, input().split()))
one_cnt = 0
two_cnt = 0
for v in S:
    two_cnt += (v // 2)
    if v % 2 == 1:
        one_cnt += 1

if sum(S) % 3 == 0 and one_cnt <= two_cnt:
    print('YES')
else:
    print('NO')
