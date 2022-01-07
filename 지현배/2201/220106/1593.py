import sys
input = sys.stdin.readline

g, len_S = map(int, input().split())
W = input().rstrip()
S = input().rstrip()
ans = 0

word_idxs = {}
word_cnt = []
idx = 0

for w in W:
    if w in word_idxs:
        word_cnt[word_idxs[w]] += 1
    else:
        word_idxs[w] = idx
        word_cnt.append(1)
        idx += 1

curr_cnt = [0] * len(word_cnt)

for i in range(g):
    if S[i] in word_idxs:
        curr_cnt[word_idxs[S[i]]] += 1

if curr_cnt == word_cnt:
    ans += 1

for i in range(g, len_S):
    if S[i - g] in word_idxs:
        curr_cnt[word_idxs[S[i - g]]] -= 1
    if S[i] in word_idxs:
        curr_cnt[word_idxs[S[i]]] += 1
    
    if curr_cnt == word_cnt:
        ans += 1

print(ans)