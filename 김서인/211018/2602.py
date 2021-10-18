magic_paper = input()
devil_bridge = input()
angel_bridge = input()

magic_paper_len = len(magic_paper)
bridge_len = len(devil_bridge)

ans = 0

bridge = [devil_bridge, angel_bridge]


def sol(start_bridge_type):
    global ans

    # DP 테이블
    dp_table = list(list([0] * magic_paper_len for _ in range(bridge_len)) for _ in range(2))
    # 어느 다리부터 시작하는지
    curr_bridge = start_bridge_type

    # 시작점으로 가능한 곳 체크
    for i in range(bridge_len):
        if magic_paper[0] == bridge[curr_bridge][i]:
            dp_table[curr_bridge][i][0] = 1

    # 이제 다음 다리로
    curr_bridge = (curr_bridge + 1) % 2

    # 천사-악마 다리 번갈아 가면서 가능한 수 체크
    for i in range(magic_paper_len):
        curr_bridge_letter = magic_paper[i]

        # 지금 찾는 다리에서 해당 문자 있는지
        for j in range(bridge_len):
            if curr_bridge_letter == bridge[curr_bridge][j]:

                # 이전 다리
                before_bridge = (curr_bridge + 1) % 2

                # 지금 다리로 올 수 있는 가능성
                for k in range(j):
                    if bridge[before_bridge][k] == magic_paper[i - 1]:
                        dp_table[curr_bridge][j][i] += dp_table[before_bridge][k][i - 1]

        curr_bridge = (curr_bridge + 1) % 2

    for i in range(bridge_len):
        ans += dp_table[0][i][magic_paper_len - 1]
        ans += dp_table[1][i][magic_paper_len - 1]


sol(0)  # 악마 다리부터 시작
sol(1)  # 천사 다리부터 시작

print(ans)
