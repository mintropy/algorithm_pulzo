import sys
input = sys.stdin.readline
month_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

id = input().rstrip()
cnt = int(input())
loc = set()
for _ in range(cnt):
    loc.add(input().rstrip())

id_loc = id[:6]
id_bir = id[6:14]
id_ord = id[14:17]
id_chk = id[17]

def sol(id, id_loc, id_bir, id_ord, id_chk):
    if not (id_loc in loc):
        return 'I'
    yun = False
    year = int(id_bir[:4])
    month = int(id_bir[4:6])
    date = int(id_bir[6:])
    if year % 4 == 0:
        yun = True
        if year % 100 == 0 and not (year % 400 == 0):
            yun = False

    if not (1900 <= year <= 2011):
        return 'I'
    if not (1 <= month <= 12):
        return 'I'
    if month == 2 and yun:
        if not (1 <= date <= 29):
            return 'I'
    else:
        if not (1 <= date <= month_end[month - 1]):
            return 'I'
    
    if id_ord == '000':
        return 'I'

    sum = 0
    x = 10 if id_chk == 'X' else int(id_chk)
    for i in range(17):
        sum += int(id[i]) * 2 ** (17 - i) % 11
    if not ((sum + x) % 11 == 1):
        return 'I'
    
    return 'M' if int(id_ord) % 2 else 'F'

print(sol(id, id_loc, id_bir, id_ord, id_chk))
