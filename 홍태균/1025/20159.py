'''
동작 그만. 밑장 빼기냐?

'''
import sys
input = sys.stdin.readline

N  = int(input())

# 홀수, 짝수번째 패
A = []
B = []

_list = list(map(int,input().split()))

# 홀수, 짝수 나눠서 담기
for i in range(N):
    if i % 2:
        B.append(_list[i])
    else:
        A.append(_list[i])

# 나한테 밑장 빼기했을 때, 
# 처음부터 밑장 빼기를 한거부터 차례로
me_list = [sum(B)]
# 상대에게 밑장 빼기했을 때,
# 밑장빼기 안한거와 끝에서 부터 밑장빼기한거 부터 앞으로
you_list = [sum(A)]

# 상대와 나에게 한번씩 밑장 빼기한 것을 저장
for i in range(1,N//2):
    # 앞으로 가면서 밑장빼기하는 인덱스를 늘리면
    # A에꺼는 더하고 B에꺼는 뺀다.
    me_list.append(me_list[i-1] + A[i-1] - B[i-1])
    # 끝에서 부터 밑장 빼기를하면 그 인덱스의 A는 빼고 B를 더해준다.
    you_list.append(you_list[i-1] - A[N//2 - i] + B[N//2 - i - 1])

# 그 중에 가장 큰거
print(max(me_list+you_list))

'''
6
3 2 5 2 1 3
'''