'''
머리 톡톡

'''
import sys
input = sys.stdin.readline

N = int(input().strip())

# 숫자 카운트를 하기 위해서
num_list = [0] * 1000001
# 각 숫자 저장
idx_list = []

# 숫자 카운트와 숫자 저장
for _ in range(N):
    n = int(input().strip())
    idx_list.append(n)
    num_list[n] += 1

result = [0] * 1000001

# 1~1000000까지 순회
for i in range(1,1000001):
    # 해당 숫자가 있는지 확인
    if num_list[i] == 0:
        continue
    # 있다면 해당 숫자의 배수에 
    # 해당 숫자의 갯수만큼 더해준다.
    for j in range(i,1000001,i):
        result[j] += num_list[i]

# 각 숫자에서 자기 자신을 빼고 출력
for i in idx_list:
    print(result[i] - 1)