import sys
input = sys.stdin.readline
P = int(input())
for t in range(1, P + 1):
    _, f = input().split()
    p, q = map(int, f.split('/'))
    p = (p // q) * q + (q - p % q)
    print(f'{t} {q}/{p}')