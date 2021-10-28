# 깊이 n인 하노이탑을 s에서 m을 거쳐 e로 옮긴다.
def hanoi(n, s, m, e):
    # 깊이가 1이면 s에서 e로 바로 옮길 수 있다.
    if n == 1: return [[s, e]]
    # 깊이 n인 하노이탑을 s에서 e로 옮기려면
    # 깊이 n-1인 하노이탑을 s에서 m으로 옮겨둬야
    # n을 s로 e로 옮길 수 있다.
    # 그 후 다시 깊이 n-1인 하노이탑을 m에서 e로 옮긴다.
    return hanoi(n - 1, s, e, m) + [[s, e]] + hanoi(n - 1, m, s, e)
arr = hanoi(int(input()), 1, 2, 3)
print(len(arr))
for a in arr:
    print(*a)
arr2 = []
def hanoi2(n, s, m, e):
    if n == 1: arr2.append([s, e])
    else:
        hanoi2(n - 1, s, e, m)
        arr2.append([s, e])
        hanoi2(n - 1, m, s, e)
hanoi2(3, 1, 2, 3)
print(arr2)