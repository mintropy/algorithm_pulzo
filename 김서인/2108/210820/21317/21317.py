import sys

input = sys.stdin.readline

N = int(input())
stones = list(tuple(map(int, input().split())) for _ in range(N - 1))
stones = [0] + stones
K = int(input())

arr = []


def dfs(idx, use_bigbig_jump, energy_sum):
    if idx == N:  # 최종 돌까지 갔을 때 든 에너지 총합을 arr에 저장 후 리턴
        arr.append(energy_sum)
        return
    elif idx > N:  # 최종 돌을 넘어가면 리턴
        return
    if use_bigbig_jump == False:  # 매우 큰 점프 안했는지 체크한 후, 매우 큰 점프 사용
        dfs(idx + 3, True, energy_sum + K)


    dfs(idx + 1, use_bigbig_jump, energy_sum + stones[idx][0])  # 작은 점프
    dfs(idx + 2, use_bigbig_jump, energy_sum + stones[idx][1])  # 큰 점프


dfs(1, False, 0)  # 몇번째 돌에 있는지, 매우 큰 점프를 했는지 안했는지, 그 돌까지 갈 때 에너지가 얼마나 들었는지
print(min(arr))  # N까지 최소 에너지 써서 가는 경우를 출력
