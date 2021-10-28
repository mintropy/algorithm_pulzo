import sys
ipt = sys.stdin.readline
N = int(ipt())

# 행복의 최댓값
maxHappy = 0

# 잃은 체력
costs = list(map(int, ipt().split()))
# 얻는 행복
happys = list(map(int, ipt().split()))

def bin(idx, HP, haha):
    # 마지막 사람까지의 경우의 수를 따지고 난 뒤
    if idx == N:
        global maxHappy
        # 최대 행복도 확인
        maxHappy = max(maxHappy, haha)
        return
    # idx번 째에게 인사 안함
    bin(idx + 1, HP, haha)
    # idx번 째에게 인사 했을 때 체력이 0이하로 떨어지면 인사 안함
    if HP - costs[idx] < 1:
        return
    # idx번 째에게 인사 함
    bin(idx + 1, HP - costs[idx], haha + happys[idx])
    
# 행복 0 체력 100에서 시작
bin(0, 100, 0)
print(maxHappy)