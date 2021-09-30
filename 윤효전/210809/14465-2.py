import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, K, B = map(int, input().split())
S = [0] * N
for _ in range(B):
    S[int(input())-1] = 1


# 초기값 지정
init_list = S[:K]
need_fix = init_list.count(1)
min_cnt = need_fix

# 인덱스 범위
left_idx = 0
right_idx = K-1

# 반복 횟수 : N-K+1
for _ in range(N-K):
    if S[left_idx] == 1:
        need_fix -= 1
    left_idx += 1
    right_idx += 1
    if S[right_idx] == 1:
        need_fix += 1
    min_cnt = min(min_cnt, need_fix)
    #print(left_idx, right_idx, need_fix)
print(min_cnt)
