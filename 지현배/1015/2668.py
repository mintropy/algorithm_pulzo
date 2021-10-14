import sys
input = sys.stdin.readline
N = int(input())
arr = [0] * (N + 1)
for n in range(1, N + 1):
    arr[n] = int(input())
ans = set()
def DFS(n):
    if arr[n] == i:
        return True
    if arr[n] in ans:
        return False
    else:
        ans.add(arr[n])
        if not DFS(arr[n]):
            ans.remove(arr[n])
            return False
        else:
            return True

for i in range(1, N + 1):
    if not i in ans:
        ans.add(i)
        if not DFS(i):
            ans.remove(i)
print(len(ans), *sorted(list(ans)), sep='\n')