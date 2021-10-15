'''
색종이와 가위

'''
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

# 이분 탐색
def bs(st,ed):
    while st <= ed:
        m = (st + ed)//2
        # 총 갯수를 계산
        # 총 갯수는 (가로 + 1) * (세로 + 1)
        A = (N - m + 1) * (m + 1)
        # K와 같다면
        if A == K:
            return "YES"
        # 작으면 오른쪽확인
        if A < K:
            st = m + 1
        # 크면 왼쪽확인
        else:
            ed = m - 1
    # 못찾으면 NO
    return "NO"

# 총 갯수가 대칭하기 때문에 반으로 나누어서 확인
print(bs(0,N//2))
