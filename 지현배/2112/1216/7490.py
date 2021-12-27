import sys
input = sys.stdin.readline
def DFS(i, n, exp):
    if i >= n:
        exp2 = exp.replace(' ', '')
        if eval(exp2) == 0:
            return [exp]
        return []
    res = []
    res.extend(DFS(i + 1, n, f'{exp} {i + 1}'))
    res.extend(DFS(i + 1, n, f'{exp}+{i + 1}'))
    res.extend(DFS(i + 1, n, f'{exp}-{i + 1}'))
    return res

T = int(input())
for _ in range(T):
    N = int(input())
    print(*DFS(1, N, '1'), sep="\n")
    print()
