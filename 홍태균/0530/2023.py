'''
신기한 소수

'''
import sys
input = sys.stdin.readline

N = int(input().strip())

# 소수 확인
def ck(n):
    # 1~루트n 까지
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            return 0

    return 1

# 탐색
def dfs(num):
    # N 자리 숫자인지
    if len(str(num)) == N:
        print(num)
        return
    # 뒤에 숫자 붙이기
    for i in range(10):
        ck_num = int(str(num) + str(i))
        if ck(ck_num):
            dfs(ck_num)

# 첫 자리 숫자
for i in range(2,10):
    if ck(i):
        dfs(i)