'''
문자 해독

'''
import sys
input = sys.stdin.readline

# 순서는 상관없기 때문에 포함하는 알파벳 갯수를 비교하였다.

g, s = map(int,input().split())
W = list(input().strip())
# W 알파벳 딕셔너리 생성
W_dict = dict()
for w in W:
    if w in W_dict.keys():
        W_dict[w] += 1
    else:
        W_dict[w] = 1

# 처음 길이 g 만큼은 먼저 시작하기 위해 
# S 알파벳 딕셔너리 생성
S = list(input().strip())
S_dict = dict()
for ss in S[:g]:
    if ss in S_dict.keys():
        S_dict[ss] += 1
    else:
        S_dict[ss] = 1

# 비교 시작
ans = 0
# 처음 시작
if W_dict == S_dict:
        ans += 1
# 한칸씩 앞으로 가면서 비교
for i in range(g,s):
    # 앞의 알파벳을 제거하는 과정
    # 1개 있으면 딕셔너리에서 제거
    if S_dict[S[i-g]] == 1:
        del S_dict[S[i-g]]
    # 2개 이상이면 1개 제거
    else:
        S_dict[S[i-g]] -= 1
    
    # 뒤의 알파벳을 추가하는 과정
    # 딕셔너리에 있으면 1개 증가
    if S[i] in S_dict.keys():
        S_dict[S[i]] += 1
    # 없으면 1로 추가
    else:
        S_dict[S[i]] = 1
    # 두 딕셔너리 비교
    if W_dict == S_dict:
        ans += 1

print(ans)

'''
defaultdict
from collections import defaultdict
import sys
input = sys.stdin.readline

len_w, len_s = map(int, input().split(" "))
W = input().strip()
S = input().strip()


W_dict = defaultdict(int)
S_dict = defaultdict(int)

for w in W:
    W_dict[w] += 1

for i in range(len_w):
    S_dict[S[i]] += 1

ans = 0
if S_dict == W_dict :
    ans += 1

for i in range(len_w, len_s):
    S_dict[S[i-len_w]] -= 1
    if S_dict[S[i-len_w]] == 0 :
        del S_dict[S[i-len_w]]
    S_dict[S[i]] += 1

    if W_dict == S_dict :
        ans += 1

print(ans)
'''