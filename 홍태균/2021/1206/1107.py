'''
리모컨

'''
import sys
input = sys.stdin.readline

N = int(input().strip())

M = int(input().strip())

# M이 있을 경우에만 받기
not_list = []
if M != 0:
    not_list = list(input().split())

# N 위로 가장 가까운 숫자 찾기
up = -1
# 대강 1000000 정도까지 구하기
for i in range(N,1000000):
    # 각 자리 숫자가 안되는 숫자 버튼에 속하는지 판단
    for j in set(str(i)):
        if j in not_list:
            break
    # 만약 모든 숫자가 안 속한다면 해당 숫자를 선택
    else:
        up = i
        break

# N 아래로 가장 가까운 숫자 찾기
down = -1
for i in range(N,-1,-1):
    # 각 자리 숫자가 안되는 숫자 버튼에 속하는지 판단
    for j in set(str(i)):
        if j in not_list:
            break
    # 만약 모든 숫자가 안 속한다면 해당 숫자를 선택
    else:
        down = i
        break

# up과 down의 여부에 따라 판단
if up > -1 and down > -1:
    print(min(abs(N - 100),len(str(up)) + up - N,len(str(down)) + abs(down - N)))
elif up > -1:
    print(min(abs(N - 100),len(str(up)) + up - N))
elif down > -1:
    print(min(abs(N - 100),len(str(down)) + abs(down - N)))
else:
    print(abs(N - 100))