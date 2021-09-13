# 맨앞부터 보면서 그게 그 다음 것보다 작으면 없애고, 크거나 같으면 냅두는 식으로 K개 제거하기
N, K =map(int,input().split())
arr = list(map(int,input()))

l = []

def sol():
    i = 0
    cnt = 0
    while i < len(arr):
        if l:
            while l and l[-1] < arr[i]: # 앞에 작은 수 다 없애기
                l.pop()
                cnt += 1
                if cnt == K:
                    return i
        l.append(arr[i])
        i+= 1
    return len(arr)
i = sol()
ans= list(l)+arr[i:]
if len(ans) == N-K:
    pass
elif len(ans) > N-K:
    ans = ans[:N-K]

print(''.join(map(str,ans)))