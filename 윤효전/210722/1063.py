# import sys
# import re
# import collections
# import itertools
# import math
# DEBUG = 1

# TC = [
#     {'data': ['A1', 'A2', '5', ['B', 'L', 'LB', 'RB', 'LT']], 'AC': 'A1\nA2'},
#     {'data': ['A1', 'B2', '2', ['R', 'T']], 'AC': 'B2\nB3'},
#     {'data': ['A1', 'B2', '2', ['T', 'R']], 'AC': 'B2\nC2'},
#     {'data': ['A1', 'B2', '2', ['L', 'LT']], 'AC': 'A1\nB2'},
# ]

# def read_data(l, in_f, out_f=None):
#     input = in_f.readline
#     #N, S = map(lambda x:x.rstrip(), in_f)
#     X, Y, N = input().rstrip().split()
#     S = list(map(lambda x:x.rstrip(), in_f))

#     data = [X, Y, N, S]
#     if DEBUG:
#         #ac = out_f.readline().rstrip()
#         ac = '\n'.join(map(lambda x:x.rstrip(), out_f))
#         l.append({'data':data, 'AC':ac})
#     else:
#         l.append({'data':data})

# def cal_pos(s):
#     x, y = s[0], s[1]
#     d = {chr(ord('A')+i) : i+1 for i in range(26)}
#     return (d[x], int(y))

# def pos_back(x, y):
#     d = {i+1 : chr(ord('A')+i) for i in range(26)}
#     return f'{d[x]}{y}'

# def is_in_boundary(x, y):
#     if y > 8 or y < 1 or x > 8 or x < 1:
#         return False
#     else:
#         return True

# def move_pos(x, y, com):
#     d_pos = {
#         'R':(0, 1), 'L':(0, -1), 'B':(-1, 0), 'T':(1, 0),
#         'RT':(1, 1), 'LT':(1, -1), 'RB':(-1, 1), 'LB':(-1, -1)
#         }

#     dy, dx = d_pos[com]
#     tmp_x, tmp_y = x+dx, y+dy
#     if is_in_boundary(tmp_x, tmp_y):
#         return (tmp_x, tmp_y)
#     else:
#         return (x, y)
    

# def solution(X, Y, N, S):
#     ans = []
#     king_x, king_y = cal_pos(X)
#     dol_x, dol_y = cal_pos(Y)
#     for s in S:
#         tmp_x, tmp_y = move_pos(king_x, king_y, s)
#         if tmp_y == dol_y and tmp_x == dol_x:
#             tmp2_x, tmp2_y = move_pos(dol_x, dol_y, s)
#             if tmp2_y == dol_y and tmp2_x == dol_x:
#                 continue
#             else:
#                 dol_x, dol_y = tmp2_x, tmp2_y
#                 king_x, king_y = tmp_x, tmp_y
#         else:
#             king_x, king_y = tmp_x, tmp_y

#     ans.append(pos_back(king_x, king_y))
#     ans.append(pos_back(dol_x, dol_y))
#     return ans_to_str(ans)

# def ans_to_str(ans):
#     if type(ans) == list:
#         return '\n'.join(map(str, ans))
#     elif type(ans) != str:
#         return str(ans)
#     else:
#         return ans

# def main():
#     if DEBUG:
#         #print_data()
#         #print(TC)
#         pass
#     else:
#         TC.clear()
#         read_data(TC, sys.stdin)
#         #read_data(TC, open('input.txt', 'r'))

#     for i, v in enumerate(TC, 1):
#         res = solution(*v['data'])
#         if DEBUG:
#             if res == v['AC']:
#                 print(f'case #{i}: OK')
#             else:
#                 print(f'case #{i}: ERR')
#                 print('accepted:')
#                 print(v['AC'])
#                 print('wrong answer:')
#                 print(res)
#         else:
#             print(res)

# def print_data():
#     with open("input.txt", 'r') as in_f, open("output.txt", 'r') as out_f:
#         tmp = []
#         read_data(tmp, in_f, out_f)
#         print(tmp)

# if __name__ == "__main__":
#     main()

import sys

def read_data(l, in_f):
    input = in_f.readline
    X, Y, N = input().rstrip().split()
    S = list(map(lambda x:x.rstrip(), in_f))

    data = [X, Y, N, S]
    l.append(data)

def cal_pos(s):
    x, y = s[0], s[1]
    d = {chr(ord('A')+i) : i+1 for i in range(26)}
    return (d[x], int(y))

def pos_back(x, y):
    d = {i+1 : chr(ord('A')+i) for i in range(26)}
    return f'{d[x]}{y}'

def is_in_boundary(x, y):
    return False if y > 8 or y < 1 or x > 8 or x < 1 else True

def move_pos(x, y, com):
    d_pos = {
        'R':(0, 1), 'L':(0, -1), 'B':(-1, 0), 'T':(1, 0),
        'RT':(1, 1), 'LT':(1, -1), 'RB':(-1, 1), 'LB':(-1, -1)
        }

    dy, dx = d_pos[com]
    tmp_x, tmp_y = x+dx, y+dy
    if is_in_boundary(tmp_x, tmp_y):
        return (tmp_x, tmp_y)
    else:
        return (x, y)
    
def solution(X, Y, N, S):
    ans = []
    king_x, king_y = cal_pos(X)
    dol_x, dol_y = cal_pos(Y)
    for com in S:
        tmp_x, tmp_y = move_pos(king_x, king_y, com)
        if tmp_y == dol_y and tmp_x == dol_x:
            tmp2_x, tmp2_y = move_pos(dol_x, dol_y, com)
            if tmp2_y == dol_y and tmp2_x == dol_x:
                continue
            else:
                dol_x, dol_y = tmp2_x, tmp2_y
                king_x, king_y = tmp_x, tmp_y
        else:
            king_x, king_y = tmp_x, tmp_y

    ans.append(pos_back(king_x, king_y))
    ans.append(pos_back(dol_x, dol_y))
    return ans_to_str(ans)

def ans_to_str(ans):
    if type(ans) == list:
        return '\n'.join(map(str, ans))
    elif type(ans) != str:
        return str(ans)
    else:
        return ans

def main():
    TC = []
    #read_data(TC, sys.stdin)
    read_data(TC, open('input.txt', 'r'))

    for case in TC:
        print(solution(*case))

if __name__ == "__main__":
    main()