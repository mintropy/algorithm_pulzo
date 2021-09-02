import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
immediate_superior_list = list(map(int, input().split()))

# 상사-부하 관계를 트리 형태로 저장
immediate_subordinate = [[] for _ in range(n + 1)]  # 직속 부하의 번호를 저장(직속 부하가 여러 명일 수도 있으니 리스트 형태로 저장)
immediate_superior = [0] * (n + 1)  # 직속 상사 번호를 저장 (직속 상사는 한 명이니까 그냥 숫자로 저장)
for i in range(1, len(immediate_superior_list)):
    immediate_subordinate[immediate_superior_list[i]].append(i + 1)
    immediate_superior[i + 1] = immediate_superior_list[i]

# 칭찬의 정보 저장하는 리스트 (인덱스 번호가 직원 번호)
compliment = [0] * (n + 1)


def dfs(n): # 순회
    compliment[n] += compliment[immediate_superior[n]]  # 직속 상사가 칭찬 받은 걸 그대로 더해서 받으면 된다!
    for i in range(len(immediate_subordinate[n])): # 그 직속 부하들까지 내려감
        dfs(immediate_subordinate[n][i])


for i in range(m):  # 입력되는 칭찬 수
    receiver, com_value = map(int, input().split())  # 칭찬 받은 직원 번호, 칭찬의 수치
    compliment[receiver] += com_value  # 일단 바로 칭찬 받은 직원이 칭찬을 받고

# 당사자가 일단 칭찬 다 받은 후에, 자식에게 전파
dfs(1)

compliment.pop(0) # 인덱스 편하게 쓰려고 처음에 0번 인덱스는 의미 없는 거라서 팝
print(*compliment)