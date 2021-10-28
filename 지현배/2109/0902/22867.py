import sys
input = sys.stdin.readline
def parsing(string):
    h, m, s_ms = string.split(':')
    s, ms = map(int, s_ms.split('.'))
    return [int(h), int(m), s, ms]

N = int(input())
time_table = [[] for _ in range(2 * N)]
for n in range(N):
    _in, _out = input().split()
    # 입차는 1 출차는 0
    time_table[2 * n] = parsing(_in) + [1]
    time_table[2 * n + 1] = parsing(_out) + [0]
time_table.sort(key=(lambda x: (x[0], x[1], x[2], x[3], x[4])))
answer = 0
curr = 0
for t in time_table:
    # 입차하면 + 1
    if (t[4] == 1): curr += 1
    # 출차하면 - 1
    else: curr -= 1
    # 최댓값이랑 비교
    answer = max(answer, curr)
print(answer)
    