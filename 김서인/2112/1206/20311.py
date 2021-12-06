import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, K  = MIIS()

reagents = list(MIIS())
reagents_name_count = []

for idx, value in enumerate(reagents):
    reagents_name_count.append([value, idx+1]) # 양, 이름

reagents_name_count.sort(reverse=True)


def sol():
    result = [0] * N

    idx = 0
    # 짝수 위치에 배치하기
    if N%2 :
        tmp = N//2+1
    else:
        tmp = N//2

    for i in range(tmp):
        result[i*2] = reagents_name_count[idx][1]
        reagents_name_count[idx][0] -= 1
        if reagents_name_count[idx][0] == 0:
            idx += 1

    # 홀수 위치에 배치
    for i in range(N//2):
        result[i*2+1] = reagents_name_count[idx][1]

        reagents_name_count[idx][0] -= 1
        if reagents_name_count[idx][0] == 0:
            idx += 1

    return result





# 불가능할 때(한 가지 색깔의 수가 나머지 색깔 수의 합 + 1 보다 크면)
max_reagent_num = reagents_name_count[0][0]
if (max_reagent_num) > (N - max_reagent_num + 1):
    print(-1)
else: # 가능할 때 -> 개수 많은 것부터 하나씩 돌아가면서 놓자.
    print(*sol())

'''

2 1 3


1 2 3 1 3 1

2 2 2
1 1
2 2
3 3

3 1 1 1
1 2 3 4 1 1

'''