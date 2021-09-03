"""
Title : 하노이 탑 이동 순서
Link : https://www.acmicpc.net/problem/11729
"""

n = int(input())

def hanoi(num, st, to, res):
    global ans
    # n - 1번 재귀 들어가면 처음 이동이 1 >> 3인지 1 >> 2인지 자동 판별
    if num == 1:
        ans.append((st, to))
        return
    hanoi(num - 1, st, res, to)
    # 첫 재귀 벗어나는 기준으로 생각
    # 가장 작은 원판이 이동한 곳 res와 다른곳으로 이동해야함
    ans.append((st, to))
    hanoi(num - 1, res, to, st)


ans = []
hanoi(n, 1, 3, 2)

print(len(ans))
for a, b in ans:
    print(a, b)
