'''
우울한 방학

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

H = list(map(int,input().split()))

# 기분을 커버 할 수 없는 날
sad_days = M - sum(H) - N

# 만약 모두 커버 할 수 있다면 우울함은 0 
if sad_days <= 0:
    print(0)
# 만약 못한다면 이를 우울함이 가장 적게 배치
# 우울함이 적게하기 위해서는 최대한 골고루 가져야함.
else:
    # 최소한 가져야하는 날들
    moc = sad_days//(N+1)
    # 다 나누고 남은 날들
    na = sad_days%(N+1)
    # 계산을 위해 각날들을 저장
    sad_list = [moc] * (N+1)
    # 남은 날들을 고루 분포
    for i in range(na):
        sad_list[i] += 1
    
    # 우울함
    mel = 0

    # 계산 n^2의 합식을 사용
    for i in sad_list:
        mel += (i*(i+1)*(2*i+1))//6

    print(mel)


