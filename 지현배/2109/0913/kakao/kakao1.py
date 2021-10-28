def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    id_map = dict()
    for id in id_list:
        id_map[id] = set()
    # good = 신고한 사람, bad = 신고당한 사람
    # 신고당한 사람의 set에 신고한 사람을 넣는다.
    for rep in report:
        good, bad = rep.split()
        id_map[bad].add(good)
    # id_list 순으로 신고당한 적이 있으면
    # 신고한 사람들의 인덱스에 해당하는 answer를 1 증가
    for id in id_list:
        if len(id_map[id]) >= k:
            for id in list(id_map[id]):
                answer[id_list.indexof(id)] += 1
    return answer
            