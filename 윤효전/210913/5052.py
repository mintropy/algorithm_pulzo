import sys
import re
import collections
import itertools
import array
DEBUG = 1

TC = [
    {'data': [2, [[3, ['911', '97625999', '91125426']], [5, ['113', '12340', '123440', '12345', '98346']]]], 'AC': 'NO\nYES'},
]

def read_data(l, in_f, out_f=None):
    input = in_f.readline
    #N, S = map(lambda x:x.rstrip(), in_f)
    T = int(input().rstrip())
    L = []
    for _ in range(T):
        N = int(input().rstrip())
        tmp = []
        for _ in range(N):
            tmp.append(input().rstrip())
        L.append([N, tmp])

    data = [T, L]
    if DEBUG:
        ac = out_f.readline().rstrip()
        #ac = '\n'.join(map(lambda x:x.rstrip(), out_f))
        l.append({'data':data, 'AC':ac})
    else:
        l.append({'data':data})

def solution(T, L):
    ans = []
    for _, l in L:
        l.sort()
        for i in range(len(l)-1):
            if l[i+1].startswith(l[i]):
                ans.append('NO')
                break
        else:
            ans.append('YES')

    ans = "\n".join(ans)
    return str(ans) if type(ans) != str else ans

def main():
    if DEBUG:
        #print_data()
        #print(TC)
        pass
    else:
        TC.clear()
        read_data(TC, sys.stdin)

    for i, v in enumerate(TC, 1):
        res = solution(*v['data'])
        if DEBUG:
            if res == v['AC']:
                print(f'case #{i}: OK')
            else:
                print(f'case #{i}: ERR')
                print('accepted:')
                print(v['AC'])
                print('wrong answer:')
                print(res)
        else:
            print(res)

def print_data():
    with open("input.txt", 'r') as in_f, open("output.txt", 'r') as out_f:
        tmp = []
        read_data(tmp, in_f, out_f)
        print(tmp)

if __name__ == "__main__":
    main()