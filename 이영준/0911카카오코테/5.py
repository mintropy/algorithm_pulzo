def solution(info, edges):
    # 간선 형태 대신 각 점의 자식을 나타내는 방식으로
    tree = [[] for _ in range(len(info))]
    for pa, ch in edges:
        tree[pa].append(ch)
    answer = 0
    followed = [False] * len(info)
    
    def dfs(now: int, prob: list, sheeps: int, wolves: int):
        nonlocal answer, tree, info, followed
        if sheeps > answer:
            answer = sheeps
        for ch in tree[now]:
            # 늑대일때
            if info[ch]:
                # 해당 늑대 자리에 가지 못할 때
                if wolves + 1 == sheeps:
                    prob.append(ch)
                # 해당 늑대 자리에 갈 수 있을 때
                else:
                    pass
            # 양일때
            else:
                # 해당 양 자리에 간 후, 그 자리에서 탐색
                # 아니면 다른 불가능했던 자리들 탐색
                followed[ch] = True
                dfs(ch, prob, sheeps + 1, wolves)
    
    
    return answer
