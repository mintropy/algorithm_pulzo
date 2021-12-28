import sys
from collections import deque
input = sys.stdin.readline

d = {
    'H':'','HE':'','LI':'','BE':'','B':'',
    'C':'','N':'','O':'','F':'','NE':'',
    'NA':'','MG':'','AL':'','SI':'','P':'',
    'S':'','CL':'','AR':'','K':'','CA':'',
    'SC':'','TI':'','V':'','CR':'','MN':'',
    'FE':'','CO':'','NI':'','CU':'','ZN':'',
    'GA':'','GE':'','AS':'','SE':'','BR':'',
    'KR':'','RB':'','SR':'','Y':'','ZR':'',
    'NB':'','MO':'','TC':'','RU':'','RH':'',
    'PD':'','AG':'','CD':'','IN':'','SN':'',
    'SB':'','TE':'','I':'','XE':'','CS':'',
    'BA':'','HF':'','TA':'','W':'','RE':'',
    'OS':'','IR':'','PT':'','AU':'','HG':'',
    'TL':'','PB':'','BI':'','PO':'','AT':'',
    'RN':'','FR':'','RA':'','RF':'','DB':'',
    'SG':'','BH':'','HS':'','MT':'','DS':'',
    'RG':'','CN':'','FL':'','LV':'','LA':'',
    'CE':'','PR':'','ND':'','PM':'','SM':'',
    'EU':'','GD':'','TB':'','DY':'','HO':'',
    'ER':'','TM':'','YB':'','LU':'','AC':'',
    'TH':'','PA':'','U':'','NP':'','PU':'',
    'AM':'','CM':'','BK':'','CF':'','ES':'',
    'FM':'','MD':'','NO':'','LR':'',
}

def bfs(start):
    visit = [0]*50000
    visit = deque()
    visit.append(start)
    while visit:
        idx = visit.popleft()
        if idx >= len(S):
            return True
        if visit[idx]:
            continue
        visit[idx] = 1
        if idx < len(S)-1 and S[idx:idx+2] in d:
            visit.append(idx+2)
        if S[idx] in d:
            visit.append(idx+1)
    return False

T = int(input())
for _ in range(T):
    S = input().rstrip().upper()
    res = bfs(0)
    if res:
        print('YES')
    else:
        print('NO')