import sys
input = sys.stdin.readline
def sol():
    A, B = map(int, input().split())
    cnt = 0
    while A <= B:
        if A == B:
            return cnt + 1
        elif B % 10 == 1:
            B //= 10
            cnt += 1
        elif B % 2 == 0:
            B //= 2
            cnt += 1
        else:
            return -1
    else:
        return -1
print(sol())