'''
이동하기 5

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

A = [0] + list(map(int,input().split()))
B = [0] + list(map(int,input().split()))

candys = 0
# 각 맥스값 저장
max_A = max(A)
max_B = max(B)

i = j = 1
# A 맥스 값이 유일하다면
if A.count(max_A) == 1:
    # 오른쪽으로 이동할 인덱스
    M_i = A.index(max_A)
    
    while i <= N and j <= M:
        # 사탕 저장
        candys += A[i] * (10 ** 9) + B[j]
        # 오른쪽으로 이동
        if i == M_i:
            # 다 이동하면 밑으로 이동
            if j == M:
                i += 1
                continue
            j += 1
        # 아니면 밑으로
        else:
            i += 1
# 맥스값이 여러 개일 경우
# 마지막 인덱스에서 오른쪽으로 이동
else:
    # 처음 맥스 인덱스
    M_i = A.index(max_A)
    # 마지막 맥스 인덱스
    re_A = list(reversed(A))
    M_li = N - re_A.index(max_A)
    # j 맥스 인덱스
    M_j = B.index(max_B)

    while i <= N and j <= M:
        candys += A[i] * (10 ** 9) + B[j]
        # 맥스인덱스에 오면 오른쪽을 이동
        if i == M_i:
            # j 맥스 인덱스에서 밑으로
            if j == M_j:
                i += 1
                continue
            j += 1
        # 마지막 맥스 인덱스에서 다시 오른쪽으로
        elif i == M_li:
            # 끝에 오면 밑으로
            if j == M:
                i += 1
                continue
            j += 1
        # 나머지는 밑으로
        else:
            i += 1

print(candys)
    