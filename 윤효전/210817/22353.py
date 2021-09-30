import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

A, D, K = map(int, input().split())
D = D / 100
K = K / 100


def solve(a, win_rate, lose_rate, ac_rate):
    if win_rate >= 1.0:
        return a*ac_rate
    else:
        # print(a*ac_rate*win_rate)
        return a*ac_rate*win_rate + solve(a+A, win_rate+win_rate*K, 1-(win_rate+win_rate*K), ac_rate*lose_rate)


print(f'{solve(A, D, 1-D, 1):.7f}')
