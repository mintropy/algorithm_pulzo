import sys
input = sys.stdin.readline

S = input().rstrip()
    
if len(set(S)) == 1:
    print(-1)
    exit()
    
for i in range(len(S)//2):
    if S[i] != S[-i-1]:
        print(len(S))
        break
else:
    print(len(S)-1)