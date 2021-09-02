import sys
ipt = sys.stdin.readline
T = int(ipt())

def sol(c, v, pref):
    voted = [[0, i] for i in range(c + 1)]
    cnt = 1
    for p in pref:
        voted[p[0]][0] += 1
    voted.sort(reverse=True)
    if voted[0][0] != voted[1][0] and voted[0][0] >= v / 2:
        return voted[0][1], cnt
    cnt += 1
    cand1, cand2 = voted[0][1], voted[1][1]
    voted2 = [0, 0]
    for pre in pref:
        for p in pre:
            if p == cand1:
                voted2[0] += 1
                break
            elif p == cand2:
                voted2[1] += 1
                break
    if voted2[0] > voted2[1]:
        return cand1, cnt
    else:
        return cand2, cnt
                
for t in range(T):
    C, V = map(int, ipt().split())
    preference = []
    for v in range(V):
        preference.append(list(map(int, ipt().split())))
    president, cnt = sol(C, V, preference)
    print(president, cnt)