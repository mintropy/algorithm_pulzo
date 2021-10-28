import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [input().rstrip() for _ in range(N)]
    arr.sort()
    for i in range(N - 1):
        length = min(len(arr[i]), len(arr[i + 1]))
        if arr[i][0:length] == arr[i + 1][0:length]:
            print("NO")
            break
    else: print("YES")