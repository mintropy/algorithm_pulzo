N = int(input())
sg_cards = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))
res = {}

for card in sg_cards:
    try:
        res[card] += 1
    except:
        res[card] = 1

ret = ''

for card in cards:
    try:
        ret += str(res[card]) + ' '
    except:
        ret += '0 '
print(ret[:-1])