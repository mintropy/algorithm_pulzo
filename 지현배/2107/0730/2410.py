N = int(input())

# f(2n + 1) = f(2n) (n > 0)
if N % 2:
    N -= 1

# f(n) = f(n - 2) + f(n / 2) (n is even number)
f = {1: 1, 2: 2}

for n in range(2, N // 2 + 1):
    f2_idx = n
    if f2_idx % 2:
        f2_idx -= 1
    f[2 * n] = f[2 * (n - 1)] + f[f2_idx]
if N == 0:
    print(1)
else:
    print(f[N] % 1000000000)