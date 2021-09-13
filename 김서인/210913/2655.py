# 입력받기
n = int(input())
bricks = []
for i in range(n):
    a, b, c = map(int, input().split())
    bricks.append([a, b, c, i + 1])  # 밑면 넓이, 높이, 무게, 들어온 순서

# 밑면 기준으로 정렬
bricks.sort(reverse=True)
# print(bricks)
dp = list([''] * 2 for _ in range(n))
dp[0] = [bricks[0][1], str(bricks[0][3])]  # 높이, 뭘 쌓은 건지

res = bricks[0][1]  # 젤 넓은 거 쌓았다
res_idx = 0  # 젤 높은 거 인덱스
for i in range(1, n):  # (넓이 큰 순서대로 벽돌 보기) i번째가 젤 위 벽돌이라고 치고
    highest = 0  # 지금까지 쌓아둔 것 중 제일 큰 높이 (i번째 벽돌을 놓을 수 있는 탑 중에 젤 높은 거)
    highest_blocks_history = '-1'
    for j in range(i):
        # 무게 체크(아래 블럭이 더 무거운지) & 높이 체크
        if bricks[j][2] > bricks[i][2] and dp[j][0] > highest:  # dp[j][0]: 벽돌 j를 쌓을 때 가능한 가장 높은 탑의 높이
            highest = dp[j][0]  # 높이 갱신
            highest_blocks_history = dp[j][1]  # 높이 히스토리(탑을 쌓기 위해 들인 블록들) 갱신

    if highest_blocks_history == '-1':  # 못 쌓으면 바닥부터 쌓아라
        dp[i][1] = str(bricks[i][3])
    else:  # 쌓으면 위에 히스토리 정보 넣기
        dp[i][1] = str(bricks[i][3]) + ' ' + str(highest_blocks_history)

    dp[i][0] = highest + bricks[i][1]  # 벽돌 i를 맨 위에 쌓았을 때, 젤 높은 높이가 뭔지 갱신
    # print(dy)

    if dp[i][0] > res:  # res는 i-1벽돌까지 쌓았을 때, 젤젤 높은 높이
        res = dp[i][0]  # res 갱신 (이제 i벽돌 쌓았을 때 젤젤 높은 높이)
        res_idx = i  # 젤 꼭대기에 있는 벽돌

ans = list(dp[res_idx][1].split())
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
