'''
숫자고르기

'''
import sys
input = sys.stdin.readline

# dfs
def dfs(v):

    # 스택과 방문 숫자
    stack = [v]
    visit_num = [v]

    # 탐색
    while stack:
        node = stack.pop()
        
        n_node = num_list[node]
        
        # 다음 숫자가 방문 했는가?
        if n_node in visit_num:
            # 방문했는데 처음 숫자와 같은가
            if n_node == v:
                return v
            return 0
        # 스택과 방문 추가
        stack.append(n_node)
        visit_num.append(n_node)
    
    return 0
            
N = int(input())

num_list = [0]
ans_list = []
cnt = 0

# 입력
for i in range(1,N+1):
    num_list.append(int(input()))

# 전체 숫자 dfs
for i in range(1,N+1):
    # 0이 아닌 자신이 반환되면
    if dfs(i):
        # 해당 숫자는 사이클에 포함되기 때문에 
        # 갯수 추가와 숫자 추가
        cnt += 1
        ans_list.append(i)
# 출력
print(cnt)
for i in ans_list:
    print(i)

###########################################################
import sys
input = sys.stdin.readline

# dfs 
def dfs(v):
    # 방문 숫자
    visit_num = [v]
    # 스택
    stack = [v]

    # 스택 탐색
    while stack:
        node = stack.pop()
        # 다음 숫자
        n_node = num_list[node]
        # 다음 숫자가 처음 숫자와 같으면 사이클이 생김
        if n_node == v:
            # 갯수는 방문 숫자의 갯수
            cnt = len(visit_num)
            # 중복을 제외하기 위해서 방문 체크
            for num in visit_num:
                visit[num] = 1
            # 갯수와 사이클에 속하는 숫자
            return (cnt,visit_num)
        
        # 만약 다음 숫자가 방문했던 숫자면 다음으로(결국 return 된다)
        if n_node in visit_num:
            continue
        # 아니라면 스택과 방문 숫자에 추가
        else:
            stack.append(n_node)
            visit_num.append(n_node)
    # 없아면 0과 빈 리스트 반환
    return (0,[])


N = int(input())

# 숫자
num_list = [0]
# 방문
visit = [0] * (N+1)
# 정답 리스트
ans_list = []

# 입력
for i in range(1,N+1):
    num_list.append(int(input()))
    # 인덱스와 숫자가 같으면 바로 방문 체크와 추가
    if i == num_list[i]:
        visit[i] = 1
        ans_list.append(i)
# 숫자와 인덱스가 같은 것은 미리 추가
max_v = sum(visit)

# 각 숫자마다 체크
for i in range(1,N+1):
    # 방문했는거면 다음으로
    if visit[i]:
        continue
    # dfs후 숫자와 리스트 받아오기
    cnt, n_list = dfs(i)
    # 숫자 추가와 리스트 추가
    max_v += cnt
    ans_list.extend(n_list)

# 정렬
ans_list.sort()

# 출력
print(max_v)
for i in ans_list:
    print(i)

'''
7
3
1
1
5
5
4
6
'''