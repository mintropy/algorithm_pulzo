'''
맹세

'''
import sys
input = sys.stdin.readline

PER_TABLE = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe',
'Cs','Ba','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn',
'Fr','Ra','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Fl','Lv',
'La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu',
'Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr']

PER_TABLE = list(map(lambda x:x.lower(),PER_TABLE))

T = int(input())

def dfs(n):
    
    global word, N

    visit1 = [0] * N
    visit2 = [0] * N
    
    stack = [n]

    while stack:
        num = stack.pop()
        if num == N:
            return 1
        if visit1[num] == 0 and word[num] in PER_TABLE:
            stack.append(num+1)
            visit1[num] = 1
        if num < N -1 and visit2[num] == 0 and word[num:num+2] in PER_TABLE:
            stack.append(num+2)
            visit2[num] = 1

    return 0



for _ in range(T):
    word = input().strip()

    N = len(word)

    if dfs(0):
        print("YES")
    else:
        print("NO")



