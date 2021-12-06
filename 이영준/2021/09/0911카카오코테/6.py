def solution(board, skill):
    n, m = len(board), len(board[0])
    # 스킬을 한번에 계산하기 위하여 누적합 배열
    # 앞의 오른쪽으로만 이동하며 계산하는 누적합
    # 뒤의 값은 중복합을 막기 위해, 아래로만 계산을 하는 값
    calc_skill = [[[0, 0] for _ in range(m + 1)] for _ in range(n + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        # 항상 degree만큼 더하면 되도록
        if type == 1:
            degree *= -1
        calc_skill[r1][c1][0] += degree
        calc_skill[r1][c1][1] += degree
        calc_skill[r1][c2 + 1][0] -= degree
        calc_skill[r1][c2 + 1][1] -= degree
        calc_skill[r2 + 1][c1][0] -= degree
        calc_skill[r2 + 1][c1][1] -= degree
        calc_skill[r2 + 1][c2 + 1][0] += degree
        calc_skill[r2 + 1][c2 + 1][1] += degree
        
    # 누적합 구현 및 확인
    answer = 0
    for i in range(n):
        for j in range(m):
            right, down = calc_skill[i][j]
            board[i][j] += right
            calc_skill[i][j + 1][0] += right
            calc_skill[i + 1][j][0] += down
            calc_skill[i + 1][j][1] += down
            if board[i][j] > 0:
                answer += 1
    return answer
