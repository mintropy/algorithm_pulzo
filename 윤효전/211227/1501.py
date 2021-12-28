import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
D = defaultdict(int)
for _ in range(N):
    tmp = input().rstrip()
    if len(tmp) > 1:
        tmp = tmp[0] + ''.join(sorted(tmp[1:-1])) + tmp[-1]
    D[tmp] += 1

M = int(input())
for _ in range(M):
    sentence = input().rstrip()
    words = sentence.split()
    ans = 1
    for word in words:
        if len(word) > 1:
            tmp_str = ''.join(sorted(word[1:-1]))
            ans *= D[word[0]+tmp_str+word[-1]]
        else:
            ans *= D[word]
        
    print(ans)