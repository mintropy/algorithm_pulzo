'''
표 정렬

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]


sort_row_list = []
for idx, num in enumerate(maps[0][:]):
    sort_row_list.append((idx,num))

sort_row_list.sort(key=lambda x:x[1])

sort_row_idx = []
for idx, _ in sort_row_list:
    sort_row_idx.append(idx)



sort_col_list = []
for idx in range(N):
    sort_col_list.append((idx,maps[idx][0]))

sort_col_list.sort(key=lambda x:x[1])

sort_col_idx = []
for idx, _ in sort_col_list:
    sort_col_idx.append(idx)



def sol():
    for i in range(N):
        for j in range(M-1):
            print(maps[i][sort_row_idx[j]],end='')
            if maps[i][sort_row_idx[j]] > maps[i][sort_row_idx[j+1]]:
                return 0
        print()
    print("#")
    for j in range(M):
        for i in range(N-1):
            print(maps[sort_col_idx[i]][j],end='')
            if maps[sort_col_idx[i]][j] > maps[sort_col_idx[i+1]][j]:
                return 0
        print()
    
    return 1

print(sol())

'''
2 1
5
1

2 5
1 2 3 4 10
6 7 8 9 5
'''