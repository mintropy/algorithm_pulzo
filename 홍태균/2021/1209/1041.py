'''
주사위

'''
import sys
input = sys.stdin.readline

N = int(input().strip())

A, B, C, D, E, F = map(int,input().split())

# N이 1일 때,
# 최대값인 면만 빼고 보여주면 된다.
if N == 1:
    print(A+B+C+D+E+F - max(A, B, C, D, E, F))
# 그렇지 않으면
# 구한다.
else:
    # 1면짜리 최소값
    min1 = min(A,B,C,D,E,F)
    # 2면짜리 최소값
    min2 = min(A+B,A+C,A+D,A+E,B+C,C+E,E+D,D+B,F+B,F+C,F+D,F+E)
    # 3면짜리 최소값
    min3 = min(A+B+C,A+C+E,A+E+D,A+D+B,F+B+C,F+C+E,F+E+D,F+D+B)

    # 각 면의 갯수에 최소값을 곱한다.
    total = min1 * ((N-1)*(N-2)*4 + (N-2)*(N-2)) + min2 * ((N-1)*4 + (N-2)*4) + min3 * 4

    print(total)