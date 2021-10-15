import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(start, end, cnt):
    if start == end:
        return cnt
    if start > end:
        return -1

    ret = dfs(start*2, end, cnt+1)
    if ret != -1:
        return ret

    ret = dfs(start*10+1, end, cnt+1)
    if ret != -1:
        return ret

    return -1


A, B = map(int, input().split())
print(dfs(A, B, 1))