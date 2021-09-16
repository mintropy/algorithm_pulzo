'''
물병

'''


import sys
#N K
N, K = map(int,sys.stdin.readline().split())

# 물병넣는 수
count = 0
# 물의 양에 대한 제한이 없어서 결국 -1이 나오는 경우가 없음.
# 그래서 K보다 작아질때 까지 반복
while 1:
    # 이진수로 바꾸면 최대한 물병을 줄일 수 있는 모양으로 출력이 되고 
    # 1이 물이 있는 물병의 역할을 한다. 그 수가 K보다 적을 때 까지
    if bin(N).count('1') <= K:
        break
    # 조건을 만족하지 못하면 
    # 물병을 하나씩 추가
    # 이부분을 줄이려면 줄일 수 있을 듯.
    N += 1
    count += 1

print(count)

'''
8388608 

9437284

'''

# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
N, K = N_,K_

answer = 0
while bin(N).count('1') > K:
    plus = 2 ** (bin(N)[::-1].index('1'))
    answer += plus
    N += plus
print(answer)
