def solution(n, info):
    # 정답 배열
    answer = []
    # 점수 차이
    point_diff = 0
    
    appeach = 0
    # 어피치 점수 구하기
    for i in range(11):
        if info[i]:
            appeach += 10 - i
    
    def dfs(lion_now, m, arrow, lion, appeach):
        nonlocal info, answer, point_diff
        # 라이언의 지금 점수판, 확인할 점수, 남은 화살 ,라이언 점수, 어피치 점수
        if m == 10:
            lion_now[10] = arrow
            if lion > appeach:
                if not lion or lion - appeach > point_diff:
                    point_diff = lion - appeach
                    answer = lion_now[::]
                elif lion - appeach == point_diff:
                    for i in range(10, -1, -1):
                        if answer[i] < lion_now[i]:
                            answer = lion_now[::]
                            break
                        elif answer[i] > lion_now[i]:
                            break
            return
        # 10 - m점을 가져갈때와 아닐때로 구분하여 탐색
        # 10 - m점을 가져갈 때
        appeach_arrow = info[m]
        if arrow > appeach_arrow:
            if info[m]:
                lion_now[m] = appeach_arrow + 1
                dfs(lion_now, m + 1, arrow - (appeach_arrow + 1), lion + 10 - m, appeach - (10 - m))
                lion_now[m] = 0
            else:
                lion_now[m] = appeach_arrow + 1
                dfs(lion_now, m + 1, arrow - (appeach_arrow + 1), lion + 10 - m, appeach)
                lion_now[m] = 0
        # 가져가지 않을 때
        dfs(lion_now, m + 1, arrow, lion, appeach)
    
    dfs([0] * 11, 0, n, 0, appeach)
    
    if not answer:
        return [-1]
    else:
        return answer