'''
걷는 건 귀찮아

'''
import sys

input = sys.stdin.readline

N, M = map(int,input().split())

rickshaw = list(map(int,input().split()))
dist = list(map(int,input().split()))

# 거리가 1000000까지
# 1행은 인력거의 유무
# 2행은 인력거의 거리
road = [[0] * 1000001 for _ in range(2)]

# 인력거의 유무는 0과 1로
for i in range(N):
    road[0][rickshaw[i]] = 1
    road[1][rickshaw[i]] = dist[i]

# 마지막 도착 지점도 도착할 수 있도록
road[0][M] = 1

# 처음 시작
idx = rickshaw[0]
# 다음 인력거 저장
next_idx = rickshaw[0]

# 인력거를 처음 타는 건 빼기위해서
cnt = -1

while 1:
    max_d = 0
    cnt += 1
    # 인력거 거리 중 다음 인력거 선택
    for i in range(1,road[1][idx]+1):
        # 범위내 인력거가 있으면
        if idx + i <= M and road[0][idx + i] == 1:
            # 더 멀리 갈 수 있는지 확인 (=는 뒤에 있는걸 선택하기 위해서)
            if max_d <= idx + i + road[1][idx + i]:
                max_d = idx + i + road[1][idx + i]
                # 더 멀리 갈 수 있어도 M을 초기화 혹시 한번에 갈 수 있는데 못가는 경우가 나올 수 있음.
                if max_d >= M:
                    max_d = M
                # 다음 인력거
                next_idx = idx + i
    # 지금 인력거와 다음 인력거가 같다면 못간다는 걸 의미
    if idx == next_idx:
        break
    
    # 원하는 거리 이상 이라면 끝
    if next_idx >= M:
        idx = M
        break
    # 아니라면 다음 인력거로 이동
    else:
        idx = next_idx

# 끝까지 도착했는지 판단
if idx == M:
    print(cnt)
else:
    print(-1)
    

'''
4 10
1 3 5 9
5 5 4 1

4 10
2 3 5 9
5 5 4 1

4 11
1 3 5 9
5 5 4 1

1 10
1
9

1 10
2
9

1 1
1
1


5 6
1 2 3 4 5
1 1 1 1 1

1 10
9
1

5 10
1 2 3 4 5
9 11 1 1 1

5 11
1 2 3 4 5
9 1 1 1 1


5 100
1 11 30 50 90
10 19 20 40 1000

4 20
1 6 11 30
10 5 9 5


'''