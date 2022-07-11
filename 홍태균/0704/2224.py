'''
명제 증명

'''
from sys import stdin
input = stdin.readline

N = int(input().strip())

INF = 987654321

V = 122 - 65 + 1

D = [[INF] * V for _ in range(V)]

for _ in range(N):
    st, _, ed = input().split()
    if st == ed:
        continue
    D[ord(st)-65][ord(ed)-65] = 1

for k in range(V):
    for i in range(V):
        for j in range(V):
            if D[i][j] >= D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]


answer = []
cnt = 0
for i in range(V):
    for j in range(V):
        if i == j:
            continue
        if D[i][j] != INF:
            cnt += 1
            answer.append(chr(i+65) + " => " + chr(j+65))

print(cnt)
for sub in answer:
    print(sub)


'''
4% i == j

14%


'''
