import sys
input = sys.stdin.readline
def sol():
    N, K = map(int, input().split())
    nmgs = set()
    nmg = N % K
    nmg10 = 1
    nmg_sum = 0
    length = len(str(N))
    i = 0
    while True:
        nmg_sum = (nmg_sum + nmg * nmg10 % K) % K
        i += 1
        nmg10 = (nmg10 * ((10 % K) ** length)) % K
        if nmg_sum == 0:
            return i
        if nmg_sum in nmgs:
            return -1
        else:
            nmgs.add(nmg_sum)
print(sol())