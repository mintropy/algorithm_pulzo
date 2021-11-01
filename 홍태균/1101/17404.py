'''
RGB거리 2

'''
import sys
iuput = sys.stdin.readline

N = int(input())

maps = [list(map(int,input().split())) for _ in range(N)]

INF = 987654321
# 처음을 각 R, G, B를 선택했을 때 각각 dp로 저장
# 그러면 2번째는 각각 R, G, B를 선택할 수 없기 때문에 무한으로 저장
Rdp = [maps[0],[INF,maps[0][0]+maps[1][1],maps[0][0]+maps[1][2]]]
Gdp = [maps[0],[maps[0][1]+maps[1][0],INF,maps[0][1]+maps[1][2]]]
Bdp = [maps[0],[maps[0][2]+maps[1][0],maps[0][2]+maps[1][1],INF]]

# 그 다음 전과 같이 비교하면 dp에 저장
for i in range(2,N):
    # 마지막은 2번째처럼 각각 R, G, B를 선택 못하기 때문에 
    # 무한으로 저장
    if i == N-1:
        Rdp.append([INF,min(Rdp[i-1][0],Rdp[i-1][2]) + maps[i][1],min(Rdp[i-1][1],Rdp[i-1][0]) + maps[i][2]])
        Gdp.append([min(Gdp[i-1][1],Gdp[i-1][2]) + maps[i][0],INF,min(Gdp[i-1][1],Gdp[i-1][0]) + maps[i][2]])
        Bdp.append([min(Bdp[i-1][1],Bdp[i-1][2]) + maps[i][0],min(Bdp[i-1][0],Bdp[i-1][2]) + maps[i][1],INF])
    # 나머지는 그대로 저장
    else:
        Rdp.append([min(Rdp[i-1][1],Rdp[i-1][2]) + maps[i][0],min(Rdp[i-1][0],Rdp[i-1][2]) + maps[i][1],min(Rdp[i-1][1],Rdp[i-1][0]) + maps[i][2]])
        Gdp.append([min(Gdp[i-1][1],Gdp[i-1][2]) + maps[i][0],min(Gdp[i-1][0],Gdp[i-1][2]) + maps[i][1],min(Gdp[i-1][1],Gdp[i-1][0]) + maps[i][2]])
        Bdp.append([min(Bdp[i-1][1],Bdp[i-1][2]) + maps[i][0],min(Bdp[i-1][0],Bdp[i-1][2]) + maps[i][1],min(Bdp[i-1][1],Bdp[i-1][0]) + maps[i][2]])

# 이렇게 마지막에 R, G, B를 선택했을 때 가장 작은 값이 답
print(min(Rdp[-1]+Gdp[-1]+Bdp[-1]))