import sys
input = sys.stdin.readline
def sol():
    _ = int(input())
    H = list(map(int, input().split()))
    # 각 물뿌리개를 몇번 사용하는지 카운트하는 변수
    g1 = 0
    g2 = 0
    # 2 물뿌리개로 최대한 키우고 나머지를 1 물뿌리개로 채움
    for h in H:
        g1 += h % 2
        g2 += h // 2
    # 두 횟수가 같다면 YES
    if g1 == g2: return 'YES'
    # 2 물뿌리개는 1 물뿌리개 2번으로 대체 가능하지만 반대의 경우에는 아님
    elif g1 > g2: return 'NO'
    # 2 물뿌리개를 1 물뿌리개로 대체했을 때 그 수가 같아질 가능성이 있다면 YES
    else:
        if (g1 + 2 * g2) % 3: return 'NO'
        else: return 'YES'
print(sol())