import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
turn = [list(map(int, input().split())) for _ in range(Q)]

n = N
length = 0
rest = 0

while n > 1:
    rest += n % 2
    n >>= 1
    length += 1

if n != 1 and rest == 0:
    length -= 1

SIZE = 2 ** (length + 1)
tree = [0] * (SIZE * 2)
depth = length + 1

def set_tree(n, s, e):
    if s >= e:
        tree[n] = arr[s - 1]
        return tree[n]
    m = (s + e) // 2
    l = set_tree(n * 2, s, m)
    r = set_tree(n * 2 + 1, m + 1, e)
    tree[n] = l + r
    return tree[n]

set_tree(1, 1, N)

def part_sum(n, s, e, l, r):
    if e < l or r < s:
        return 0
    if l <= s and e <= r:
        return tree[n]
    m = (s + e) // 2
    return part_sum(n * 2, s, m, l, r) + part_sum(n * 2 + 1, m + 1, e, l, r)

def change_value(n, s, e, idx, value):
    if idx == s == e:
        diff = value - tree[n]
        tree[n] = value
        return diff
    m = (s + e) // 2
    if m < idx:
        diff = change_value(n * 2 + 1, m + 1, e, idx, value)
        tree[n] += diff
    else:
        diff = change_value(n * 2, s, m, idx, value)
        tree[n] += diff
    return diff

for i in range(Q):
    x, y, a, b = turn[i]
    if x > y:
        x, y = y, x
    print(part_sum(1, 1, N, x, y))
    change_value(1, 1, N, a, b)


