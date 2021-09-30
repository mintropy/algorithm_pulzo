import itertools
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
hp_list = list(map(lambda x: x[0], S))
atk_list = list(map(lambda x: x[1], S))
ans = 0


def chk(l):
    ret = 0
    for v in l:
        if v <= 0:
            ret += 1
    return ret


for v in itertools.product(range(N), repeat=N):
    tmp = hp_list[::]
    for i in range(N):
        if i == v[i]:
            continue
        if tmp[i] <= 0 or tmp[v[i]] <= 0:
            continue
        tmp[i] -= atk_list[v[i]]
        tmp[v[i]] -= atk_list[i]

    if ans < chk(tmp):
        ans = chk(tmp)
        print(ans, tmp, v)
    #ans = max(ans, chk(tmp))
    #print(ans, tmp, v)

print(ans)
