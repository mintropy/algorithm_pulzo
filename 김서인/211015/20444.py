import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# k 중에 가로 몇 번 잘랐는지를 이분 탐색으로
start = 0
end = n//2

ans = 'NO'
while start <= end:
    mid = (start + end) // 2
    garo_cnt = mid
    sero_cnt = n - mid
    paper_cnt = (garo_cnt + 1) * (sero_cnt + 1)

    if paper_cnt == k:
        ans = 'YES'
        break
    elif paper_cnt > k:  # 수가 목표보다 많으면
        end = mid - 1
    else:
        start = mid + 1

print(ans)
