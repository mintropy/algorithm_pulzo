'''
선 긋기

'''
import sys
input = sys.stdin.readline

N = int(input())

total = 0

lines = [tuple(map(int,input().split())) for _ in range(N)]
# 시작점을 기준으로 정렬
lines.sort()

# 처음 선을 가지고 시작
st, ed = lines[0]

# 다음 선부터 판단
for i in range(1,N):
    # 현재 선의 시작, 끝
    a, b = lines[i]

    # 현재 시작이 지금까지의 선에 포함이 되면 
    # 현재 선은 지금까지의 선에 포함되거나 연장시킨다.
    if st <= a <= ed:
        # b가 더 크면 연장
        # ed가 크면 포함
        ed = max(b,ed)
    
    # 포함되거나 연장시키지 않으면 끊어진거기 때문에
    # 지금까지의 선 길이를 저장하고 새로 시작
    else:
        total += ed - st
        st, ed = a, b

# 마지막 선의 길이를 저장
total += ed - st

print(total)


'''
6 
1 10
9 11
2 5
13 15
16 17
16 18

14


1
4 5
'''