import sys
input = sys.stdin.readline
N = int(input())
arr = [[] for _ in range(N)]
for n in range(N):
    x, r = map(int, input().split())
    arr[n] = (x - r, x + r)
arr.sort()
stack = []
def sol():
    for n in range(N):
        if not stack:
            stack.append(arr[n])
        else:
            while stack:
                # 스택끝의 원의 오른쪽 < 현재 원의 왼쪽
                if stack[-1][1] < arr[n][0]:
                    stack.pop()
                else:
                    # 두 원의 왼쪽이 내접하거나, 두 원이 접하거나 교차한다면 NO
                    if stack[-1][0] == arr[n][0] or arr[n][0] <= stack[-1][1] <= arr[n][1]:
                        return "NO"
                    break
            stack.append(arr[n])
    else:
        return "YES"
print(sol())