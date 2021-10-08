'''
Moo 게임

'''
import sys
input = sys.stdin.readline

N = int(input())

# S(k) 저장
S = [3]
k = 0
# 인덱스로 찾기 위해 -1을 해주었다
N -= 1

# 어떤 S(k)에 속하는 지 찾기
while S[k] <= N:
    k += 1
    S.append(S[k-1] * 2 + (k + 2) + 1)

# k를 줄여가며 분할하면서 어디에 속하는 지 파악
while k > 0:
    # 앞의 S(k-1)에 속하면 k만 줄인다
    if N < S[k-1]:
        pass
    # 뒤의 S(k-1)에 속하면 앞의 길이 만큼 인덱스를 줄이고
    # 그안에서 찾는다.
    elif N >= S[k-1] + (k + 2) + 1:
        N -= S[k-1] + (k + 2) + 1
    # m + o * (k + 1)에 속하면 바로 나온다.
    else:
        N -= S[k-1]
        break
    k -= 1

# 여기에 오는거면 S(0) 즉, 'moo'나 m + o * (k + 1)에 속한다.
# 그렇기 때문에 처음이 아니면 o 처음이면 m
if N == 0:
    print('m')
else:
    print('o')