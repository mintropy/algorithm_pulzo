'''
회문은 회문아니야!!

'''
import sys
input = sys.stdin.readline
word = list(input().strip())
N = len(word)

# 총 3가지 경우가 있다고 생각
def sol():
    # 첫번째, 처음과 끝이 달라 회문이 아닐경우
    # 전체 길이가 가장 긴 회문아닌 경우
    if word[0] != word[-1]:
        return N
    
    # 두번째, 다 같은 경우에만 안되는 경우이기 때문에
    # 다 같으면 -1
    for i in range(1,N):
        if word[0] != word[i]:
            break
    else:
        return -1
    
    # 세번째, 회문 확인 후 회문아닐 때는 첫번째 경우와 같음
    # 회문인 경우 1개만 빼도 회문이 아니게 되기때문에 N-1
    for i in range(N//2):
        if word[i] != word[N-i-1]:
            return N
    else:
        return N-1

print(sol())
    
    
    
