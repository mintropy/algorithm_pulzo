import sys
input = sys.stdin.readline

N, M = map(int, input().split())
location = list(map(int, input().split()))
negative = list(filter(lambda x: x < 0, location))
positive = list(filter(lambda x: x > 0, location))
negative.sort()
positive.sort(reverse=True)

cnt = []

idx = 0
while idx < len(negative):
    cnt.append(-negative[idx])
    idx += M

idx = 0
while idx < len(positive):
    cnt.append(positive[idx])
    idx += M

cnt.sort(reverse=True)

ans = -cnt[0]
for c in cnt:
    ans += 2 * c

print(ans)