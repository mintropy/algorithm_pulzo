'''
인내의 도미노 장인 호석

'''
import sys

input = sys.stdin.readline

N, M, R = map(int,input().split())

domino_h = [list(map(int,input().split())) for _ in range(N)]

domino = [['S'] * M for _ in range(N)]

# E W N S
dirs = {'E':(0,1),'W':(0,-1),'N':(-1,0),'S':(1,0)}
cnt = 0

for _ in range(R):
    X, Y, D = input().split()
    X, Y = int(X) - 1, int(Y) - 1
    
    dir = dirs[D]
    H = domino_h[X][Y]
    if domino[X][Y] == 'F':
        pass
    else:
        while H > 0:

            if domino[X][Y] == 'S':
                H = max(H - 1, domino_h[X][Y] - 1)
                cnt += 1
            else:
                H -= 1
            domino[X][Y] = 'F'
            
            X, Y = X + dir[0], Y + dir[1]
            
            if 0 <= X < N and 0 <= Y < M:
                pass
            else:
                break
    
    X, Y = map(int,input().split())
    X, Y = X - 1, Y - 1

    domino[X][Y] = 'S'

print(cnt)
for do in domino:
    print(*do)
    
'''
5 5 1
1 1 1 1 1
1 2 2 1 1
5 1 2 2 2
1 3 2 1 1
1 3 3 1 1
3 1 E
2 5
5 3 N
3 3
5 2 N
3 1

'''