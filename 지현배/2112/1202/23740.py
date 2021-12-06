import sys
input = sys.stdin.readline

N = int(input())
line = [tuple(map(int, input().split())) for _ in range(N)]
line.sort()

start = line[0][0]
end = line[0][0]
low = 10 ** 9 + 1

cnt = 0
ans = []
for ln in line:
    if ln[0] > end:
        cnt += 1
        ans.append(f'{start} {end} {low}')
        start = ln[0]
        end = ln[1]
        low = ln[2]
    else:
        end = max(end, ln[1])
        low = min(low, ln[2])
else:
    cnt += 1
    ans.append(f'{start} {end} {low}')

print(cnt)
print(*ans, sep="\n")
