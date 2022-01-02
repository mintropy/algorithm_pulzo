'''
휴먼 파이프라인

'''
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
people = list(map(int,input().split()))
# 정렬
people.sort()

# 맥스 v 저장
max_v = 0
# 2번째 부터 시작
for i in range(1,N):
    # 인덱스를 기준으로 나누기
    # 한칸씩가면서 정렬이 되어있기 때문에 가장 앞과 인덱스의 값이 가장 작은 값
    # 그래서 v를 첫번째 값에 인덱스에 인덱스값에 나머지 사람
    v = people[0] * i + people[i] * (N-i)
    
    # 맥스 저장
    if max_v < v:
        max_v = v

# 나머지가 있으면 1 더하기
if K % max_v:
    print(K//max_v + 1)
else:
    print(K//max_v)