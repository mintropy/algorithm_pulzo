'''
삼각형 게임

'''
import sys

input = sys.stdin.readline

def dfs(n,now,sum_v):
    global total
    
    # 6개의 삼각형을 다 탐색했으면 
    if n == 6:
        # 마지막 삼각형과 첫번째 삼각형이 
        # 이어지는지 확인
        if tris[0][cnt] == now:
            total = sum_v
        else:
            total = 0
        return
    
    # 6개의 삼각형 탐색
    for i in range(6):
        if visit[i] == 1:
            continue
        # 3개의 숫자 확인
        for j in range(3):
            # 이어지는가 확인
            if now == tris[i][j]:
                visit[i] = 1
                # 다음의 숫자는 더하고
                # 다다음 숫자와 이어지는 삼각형을 찾기위해 전달
                dfs(n+1,tris[i][(j+2)%3],sum_v+tris[i][(j+1)%3])
                visit[i] = 0

while 1:
    tris = []
    for _ in range(6):
        tris.append(list(map(int,input().split())))
    max_v = 0
    
    visit = [0] * 6
    
    # 3개의 숫자중 하나씩 선택
    for cnt in range(3):
        total = 0
        dfs(0,tris[0][cnt],0)
        if max_v < total:
            max_v = total
            
    # max_v 가 0 이면 어떤 방법으로도
    # 못만드다는 것이기 때문에 none
    if max_v:
        print(max_v)
    else:
        print('none')
    
    # 다음 입력
    next = input().strip()
    if next == "*":
        pass
    elif next == "$":
        break