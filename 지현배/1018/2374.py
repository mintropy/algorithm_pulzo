import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

ans = 0
stack = [arr[0]]
for i in range(1, N):
    last = stack[-1]
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if last <= arr[i]:
        ans += arr[i] - last
    stack.append(arr[i])
if len(stack) > 1:
    ans += stack[0] - stack[-1]
print(ans)

ans2 = 0
def DNC(s, e):
    if s >= e:
        return arr[s]
    
    max_idx = -1
    max_value = -1
    for i in range(s, e + 1):
        if arr[i] > max_value:
            max_value = arr[i]
            max_idx = i

    global ans2
    if max_idx > s:
        k = DNC(s, max_idx - 1)
        ans2 += max_value - k
        # ans2 += max_value - DNC(s, max_idx - 1)
    if max_idx < e:
        k = DNC(max_idx + 1, e)
        ans2 += max_value - k
        # ans2 += max_value - DNC(max_idx + 1, e)

    return max_value
DNC(0, N - 1)
print(ans2)