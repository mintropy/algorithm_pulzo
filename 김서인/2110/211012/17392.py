# 0이하면 ok (우울함 안 느낌)
# 일단 1일 때 약속 시작하고, -1될 때 또 약속 있게 하기.
# 몰려서 외로운 것보다는 최대한 분배해서 외롭게....

N, M = map(int, input().split())
arr = list(map(int, input().split()))

if sum(arr) + N >= M:  # 매일 행복할 수 있으면(기분이 마이너스로 안 가면)
    ans = 0
else:
    m = M  # 남은 방학
    mood = 0  # 기분
    idx = 0
    while m > 0:
        mood -= 1
        if mood <= -1:
            if idx < N:  # 기분이 0이고 약속 있으면 그 약속 배치하기
                mood = arr[idx]
                idx += 1
            else:
                break
        m -= 1  # 하루 더 지났다.
    cnt = m  # 우울한 날

    # 외로운 시간을 최대한 나누기 !
    ans = 0
    idx = 1
    jegop_hal_su = 1
    while idx <= cnt:
        for i in range(N + 1):
            if idx > cnt:
                break
            ans += jegop_hal_su ** 2
            idx += 1
        jegop_hal_su += 1



print(ans)
