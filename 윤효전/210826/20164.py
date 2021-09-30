import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def cnt_odd(s):
    ret = 0
    for c in s:
        if c in '13579':
            ret += 1
    return ret


def dfs(s, n):
    global my_min
    global my_max
    start, end = 0, len(s)-1
    n += cnt_odd(s)
    if end == 1:
        a = int(s[0])
        b = int(s[1])
        dfs(str(a+b), n)
    elif end == 0:
        my_min = min(my_min, n)
        my_max = max(my_max, n)
        return
    else:
        for i in range(start+1, end):
            for j in range(i, end):
                a = int(s[start:i])
                b = int(s[i:j+1])
                c = int(s[j+1:end+1])
                dfs(str(a+b+c), n)


my_min = float('inf')
my_max = 0
S = input().rstrip()

dfs(S, 0)
print(my_min, my_max)
