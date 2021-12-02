N = int(input())
developers = list(map(int, input().split()))
# developers.sort()

left = 0
right = len(developers) - 1
ans = 0

while left + 1 < right:
    if developers[left] < developers[right]:  # 왼쪽이 더 작음. 그럼 왼쪽 고정한 상태로 오른쪽을 줄이면 값이 줄어들 수 밖에. 왼쪽을 이동시키자.
        left += 1
        ans = max(ans, (right - left - 1) * min(developers[left], developers[right]))
    else:
        right -= 1
        ans = max(ans, (right - left - 1) * min(developers[left], developers[right]))

print(ans)

# for left in range(N-2):
#     for right in range(left+2,N):
#
#         ans = max(ans, (right-left-1)*min(developers[left], developers[right]))
