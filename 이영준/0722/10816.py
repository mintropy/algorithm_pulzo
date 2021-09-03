from sys import stdin
from collections import defaultdict, deque
n = int(stdin.readline().rstrip())
sg = list(map(int, stdin.readline().rstrip().split()))
m = int(stdin.readline().rstrip())
target = list(map(int, stdin.readline().rstrip().split()))

dic = defaultdict(int)

# for x in sg:
#     if x in dic:
#         dic[x] += 1
#     else:
#         dic[x] = 1

for x in sg:
    dic[x] += 1

# for y in target:
#     if y in dic:
#         print(dic[y])
#     else:
#         print(0, end = ' ')

for y in target:
    print(dic[y])