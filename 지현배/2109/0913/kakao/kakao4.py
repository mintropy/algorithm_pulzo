def solution(n, info):
    answer = [-1]
    arr = [0 for _ in range(11)]
    maxD = 0
    def compare(ry, ap):
        rscore, ascore = 0
        # 점수 계산
        for i in range(10):
            if ry[i] == 0 and ap[i] == 0: continue
            elif ry[i] > ap[i]: rscore += 10 - i
            else: ascore += 10 - i
        nonlocal maxD, answer
        # 라이언이 이기면서 점수차가 최댓값보다 클때
        if rscore > ascore and maxD < rscore - ascore:
            answer = arr[::]
            maxD = rscore - ascore
        # 라이언이 이기면서 점수차가 최댓값과 같을 때
        elif rscore > ascore and maxD == rscore - ascore:
            # 작은 점수가 많은 쪽을 택한다.
            for i in range(10, -1, -1):
                # 새로운 답이 더 작은 점수가 많을 때
                if arr[i] > answer[i]:
                    answer = arr[::]
                    break
                # 기존 답이 더 작은 점수가 많을 때
                elif arr[i] < answer[i]: break
    def DFS(idx, cnt):
        # 종료 조건
        # 화살을 다 쐈을 때
        if cnt <= 0:
            compare(arr, info)
            return
        # 인덱스 넘어갈 때
        if idx > 10: return
        for i in range(cnt, -1, -1):
            arr[idx] += 1
            DFS(idx + 1, cnt - i)
            arr[idx] -= i
    DFS(0, n)
    return answer