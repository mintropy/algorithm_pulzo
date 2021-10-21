import sys
input = sys.stdin.readline
N, C = map(int, input().split())
cards = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    _, *card = map(int, input().split())
    cards[i] = card
operators = [[]] + [input().rstrip().split(',') for _ in range(C)]
visited = [0] * (N + 1)
ans = set()

def DFS(n, string):
    if n >= C:
        if string:
            ans.add(string)
        else:
            ans.add('EMPTY')
        return

    for i in range(1, N + 1):
        if visited[i] < len(cards[i]):
            next = string
            for k in operators[cards[i][visited[i]]]:
                op, s = k.split()
                if op == 'ADD':
                    next += s
                else:
                    j = int(s)
                    if j >= len(next):
                        ans.add('ERROR')
                        break
                    else:
                        next = next[:j] + next[j + 1:]
            else:
                visited[i] += 1
                DFS(n + 1, next)
                visited[i] -= 1
DFS(0, '')
print(*sorted(list(ans)), sep='\n')