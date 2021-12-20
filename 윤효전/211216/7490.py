import sys
input = sys.stdin.readline

T = int(input())

def dfs(N, i, ac):
    if i == N:
        if eval(ac.replace(' ', '')) == 0:
            print(ac)
        return
    dfs(N, i+1, f'{ac} {i+1}')
    dfs(N, i+1, f'{ac}+{i+1}')
    dfs(N, i+1, f'{ac}-{i+1}')

for _ in range(T):
    N = int(input())
    dfs(N, 1, '1')
    print()