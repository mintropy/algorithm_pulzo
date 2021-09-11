import sys
input = sys.stdin.readline
N, K = map(int, input().split())
num = input().rstrip()
stack = []
# 앞에서부터 두 수를 비교하며 감소하는 수를 만든다.
for n in num:
    while True:
        if stack and stack[-1] < n and K:
            stack.pop()
            K -= 1
        else:
            stack.append(n)
            break
# K가 남아있다면 그만큼 뒤에서 뺀다.
while K:
    stack.pop()
    K -= 1
print(''.join(stack))