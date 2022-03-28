'''
성싶당 밀키트

'''
import sys
input = sys.stdin.readline

N, G, K = map(int,input().split())

kits = [list(map(int,input().split())) for _ in range(N)]

def check(x):
    O_list = []
    cnt = 0
    for i in range(N):
        s = kits[i][0] * max(1,x-kits[i][1])
        if kits[i][2]:
            O_list.append(s)
        else:
            cnt += s
    
    O_list.sort(key=lambda x:-x)
    if len(O_list) > K:
        cnt += sum(O_list[K:])

    # print(cnt)
    if cnt > G:
        return 0
    else:
        return 1
    

l = 0
r = 2*(10**9) + 1

while l <= r:
    mid = (l+r)//2
    # print("!!",l,r,mid)
    if check(mid):
        # print('l',l,r,mid)
        l = mid + 1
    else:
        # print('r',l,r,mid)
        r = mid - 1

print(r)