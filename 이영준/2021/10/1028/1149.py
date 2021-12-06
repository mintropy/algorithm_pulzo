from sys import stdin

n = int(stdin.readline())

dp = []

for _ in range(n):
    r, g, b = map(int, stdin.readline().split())
    if dp == []:
        dp.append((r, g, b))
        continue
    # n - 1 번째을 해당 색으로 칠하는 최솟값
    red, green, blue = dp[-1]
    tmp = []

    tmp.append(min(blue + r, green + r))
    tmp.append(min(red + g, blue + g))
    tmp.append(min(red + b, green + b))
    dp.append(tmp)
print(dp)
print(min(dp[-1]))