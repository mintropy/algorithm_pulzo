import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    check = [False for _ in range(N + 1)]
    for _ in range(N - 1):
        parent, children = map(int, input().split())
        tree[children] = parent
    n1, n2 = map(int, input().split())
    ptr = n1
    while True:
        check[ptr] = True
        if tree[ptr] == 0: break
        ptr = tree[ptr]
    ptr = n2
    while True:
        if check[ptr] == True: break
        ptr = tree[ptr]
    print(ptr)