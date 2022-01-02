'''
사이클 게임

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

# 부모 저장
p = list(range(N))
# 랭크 저장
rank = [0] * N

# find 함수
def find_set(x): 
    if p[x] != x: 
        p[x] = find_set(p[x]) 
    return p[x]

# union 함수
def union(x, y): 
    Link(find_set(x),find_set(y)) 

# Link 함수
def Link(x,y): 
    if rank[x] >= rank[y]: 
        p[y] = x 
    else: 
        p[x] = y 
    if rank[x] == rank[y]: 
        rank[x] += 1

# 하나씩 하면서 1번째 부터 M번째까지
for i in range(1,M+1):
    x, y = map(int,input().split())
    
    # 같으면 연결된다는 것이기 때문에 사이클이 생기는 것
    if find_set(x) == find_set(y):
        # 몇 번째인지 출력
        print(i)
        break
    # 같지 않다면 합치기
    union(x,y)
# 사이클이 없다면 0
else:
    print(0)


