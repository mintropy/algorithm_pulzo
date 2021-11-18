import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if N % 2: # 홀수면 -> 나 로 끝나서 나가 이김
        print('koosaga')
    else:  # 짝수면 -> 나(시작하는 사람) 너 나 너 ....로 끝나서 너가 이김
        print('cubelover')
