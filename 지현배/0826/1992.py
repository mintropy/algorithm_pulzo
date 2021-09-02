import sys
input = sys.stdin.readline
N = int(input())
pic = [input().rstrip() for _ in range(N)]
def dnc(n, i, j):
    # 제일 작은 요소로 쪼개지면 그걸 반환한다.
    if n == 1:
        return pic[i][j]
    n = n // 2
    # 왼쪽위,오른쪽위,왼쪽아래,오른쪽아래의 값을 가져와서
    lt = dnc(n, i, j)
    rt = dnc(n, i, j + n)
    lb = dnc(n, i + n, j)
    rb = dnc(n, i + n, j + n)
    # 그게 제일 작은요소일 때 그게 다 같다면 그 중 한 값을 반환한다.
    if len(lt) == 1 and (lt == rt == lb == rb):
        return lt
    # 아니면 나열하고 합친다.
    else:
        return "(" + lt + rt + lb + rb + ")"
print(dnc(N, 0, 0))
