a, d, k = map(int, input().split())

win_pro = d / 100
lose_pro = (1 - win_pro)
ans = win_pro  # 끝말잇기 진행하는 횟수 기댓값
cnt = 1
while True:
    cnt += 1

    win_pro = win_pro + win_pro * (k / 100)  # 이길 확률
    if win_pro >= 1:  # 이길 확률 100% 이상이면 (그럼 이길 확률 100%로 취급하니까,,)
        win_pro = 1

    ans += lose_pro * win_pro * cnt  # 이번에 이길 확률(이전에 쭉 질 확률 * 지금 이길 확률)* 횟수를 ans에 더함
    lose_pro = lose_pro * (1 - win_pro)  # 이번에 질 확률(이전에 쭉 질 확률 * 지금 질 확률)

    if win_pro == 1:
        break

print('%.7f' % (ans * a))  # 끝말잇기 진행하는 시간의 기댓값
