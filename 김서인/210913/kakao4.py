n, info = 10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
import itertools

def solution(n, info):
    answer = [-1]
    # 모든 경우의 수
    lion_result_combinations = list(itertools.combinations_with_replacement(list(range(11)), n))
    lion_result = []
    for j in range(len(lion_result_combinations)):
        tmp = [0] * 11
        for i in range(n):
            tmp[10 - lion_result_combinations[j][i]] += 1
        lion_result.append(tmp)
    print(lion_result)

    gap = 0
    # 점수 계산(10~1점 과녁 순으로 누가 더 많은지)
    for j in range(len(lion_result)):  # 각각 경우를 비교해보자
        apeach_total = 0
        lion_total = 0

        for i in range(10): # 1~ 10점 누가 얻는지
            score = 10 - i
            apeach = info[i]
            lion = lion_result[j][i]

            if lion == 0 and apeach == 0:
                continue
            elif lion > apeach:
                lion_total += score
            elif lion <= apeach:
                apeach_total += score

        if lion_total > apeach_total: # 라이언이 클 때 갱신
            if lion_total - apeach_total > gap:
                answer = lion_result[j]
                gap = lion_total - apeach_total

    return answer

print(solution(n,info))

# 패스!