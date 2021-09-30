import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def reflection(typ, k):
    res = None
    if typ == '/':
        res = {'U': 'R', 'R': 'U', 'D': 'L', 'L': 'D'}[k]
    else:
        res = {'U': 'L', 'R': 'D', 'D': 'R', 'L': 'U'}[k]
    return res


def send_sig(py, px, k):
    res = 0
    while 0 <= py < R and 0 <= px < C:
        if k in visit[py][px]:  # 무한 반복
            return -1
        else:
            visit[py][px].add(k)

        if S[py][px] in r'\/':  # 행성
            # 방향 변경
            k = reflection(S[py][px], k)
        elif S[py][px] == 'C':  # 블랙홀
            break
        else:
            pass

        res += 1
        py += d[k][0]
        px += d[k][1]

    return res


R, C = map(int, input().split())
S = [input().rstrip() for _ in range(R)]
PY, PX = map(lambda x: int(x)-1, input().split())

d = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}

ans = ['', 0]
for k, v in d.items():
    visit = [[set() for _ in range(C)] for _ in range(R)]
    tmp = send_sig(PY, PX, k)
    if tmp == -1:
        ans[1] = 'Voyager'
        ans[0] = k
        break
    else:
        if tmp > ans[1]:
            ans[1] = tmp
            ans[0] = k

print(*ans, sep='\n')
