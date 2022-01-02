'''
가장 가까운 공통 조상

'''
import sys
T = int(sys.stdin.readline().strip())

# 조상 찾기
def listpar(node):
    plist = []
    while node != 0:
        plist.append(node)
        node = tree[node]
    return plist

for _ in range(T):
    N = int(sys.stdin.readline().strip())

    tree = [0 for _ in range(N+1)]

    # 트리 그리기
    for _ in range(1,N):
        A, B = map(int,sys.stdin.readline().strip().split())
        tree[B] = A
    
    # 각각의 시작을 저장
    st, ed = map(int,sys.stdin.readline().strip().split())
    
    # 각각의 조상 리스트
    # 처음 0은 어느 한 리스트의 시작점이 공통 조상일 때를 위해서
    A_list = [0] + listpar(st)
    B_list = [0] + listpar(ed)

    # 루트 부터 찾기 위해서 cnt 사용
    cnt = 1
    while A_list[-cnt] == B_list[-cnt]:
        cnt += 1
    # 분기점 바로 전이 최소 공통
    print(A_list[-cnt+1])





'''
2
16
1 14
8 5
10 16
5 9
4 6
8 4
4 10
1 13
6 15
10 11
6 7
10 2
16 3
8 1
16 12
16 7
5
2 3
3 4
3 1
1 5
3 5
'''