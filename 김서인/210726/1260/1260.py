from collections import deque

def DFS(idx):
  if idx < 1 or idx > n:
    return
  else:
    can_go = l[idx]
    for i in range(len(can_go)):
      if chk[can_go[i]] ==0:
        print(can_go[i],end = ' ')
        chk[can_go[i]] = 1
        DFS(can_go[i])
        

def BFS(idx):
    print(idx, end=' ')
    chk[idx] = 1
    dq.append(idx)
    while dq:
      tmp = dq.popleft()
      can_go = l[tmp]
      for i in range(len(can_go)):
        if chk[can_go[i]] == 0:
          print(can_go[i], end=' ')
          chk[can_go[i]] = 1
          dq.append(can_go[i])

if __name__ == '__main__':
  n, m, v = map(int,input().split())
  l=list([] for _ in range(n+1))
  chk = [0] * (n+1) # 정점 방문했는지 체크할 리스트

  # 양방향 연결 
  for i in range(m):
    a, b =map(int,input().split())
    l[a].append(b)
    l[b].append(a)

  # 정렬(방문 가능한 정점 여러개라면 정점 번호 작은 것 먼저 방문해서)
  for i in l:
    i.sort()
  
  # DFS
  print(v, end=' ')
  chk[v] = 1
  DFS(v)
  print()


  # BFS
  chk = [0] * (n+1) # 정점 방문했는지 체크할 리스트
  dq = deque()

  BFS(v)










