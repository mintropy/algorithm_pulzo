import sys
import itertools
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
*S, L = map(lambda x:x.rstrip(), sys.stdin)

total = 0
d = {}
for l in S:
    total += len(l)
    if len(l) == 1:
        d[l[0]] = {'ready':True, 'next':None}
        continue
    for k, v in itertools.zip_longest(l, l[1:], fillvalue=None):
        d[k] = {'ready':False, 'next':v}
    d[l[0]]['ready'] = True

if total != len(L):
    print('Impossible')
    exit()

for s in L:
    if s not in d or d[s]['ready'] == False:
        print('Impossible')
        break
    else:
        d[s]['ready'] = False
        next_word = d[s]['next']
        if next_word == None:
            continue
        d[next_word]['ready'] = True
else:
    print('Possible')