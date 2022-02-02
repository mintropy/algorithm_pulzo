'''
휴게소 세우기

'''
import sys
input = sys.stdin.readline

N, M, L = map(int,input().split())

rest_areas = list(map(int,input().split()))
# 거리를 구하기 위해서 고속도로의 각 끝을 넣어준다.
rest_areas.extend([0,L])
rest_areas.sort()

# 최소값은 차이가 1 최댔값은 L
l = 1
r = L

while l <= r:
    mid = (l + r)//2
    cnt = 0
    for i in range(1,N+2):
        # 각 거리에 몇개의 휴게소가 들어가는지 확인
        dist = rest_areas[i] - rest_areas[i-1]
        # 딱 나누어 떨어지면 휴게소가 하나 줄어들기 때문에
        if dist % mid:
            cnt += dist//mid
        else:
            cnt += (dist//mid - 1)
    
    if cnt > M:
        l = mid + 1
    else:
        r = mid - 1
print(l)
            
            
'''
if L - 1 - N > M:
    while l <= r:
        mid = (l + r)//2
        if mid == 0:
            break
        cnt = 0
        for i in range(1,N+2):
            dist = rest_areas[i] - rest_areas[i-1]
            if dist % mid:
                cnt += dist//mid
            else:
                cnt += (dist//mid - 1)
        
        if cnt > M:
            l = mid + 1
        else:
            r = mid - 1
    print(l)
else:
    print(0)

'''

'''
2 7 10
1 9

1 100 50
10
'''