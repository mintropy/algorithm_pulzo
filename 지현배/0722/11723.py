import sys

M = int(sys.stdin.readline().split()[0])

S = 0

for m in range(M):
    operator = sys.stdin.readline().split()
    if operator[0] != 'all' and operator[0] != 'empty':
        num = int(operator[1])
    operator = operator[0]
        
    if operator == 'add':
        if (S & 1 << (num - 1) == 0):
            S += 1 << (num - 1)
    elif operator =='remove':
        if (S & 1 << (num - 1) > 0):
            S -= 1 << (num - 1)
    elif operator == 'check':
        print(1 if S & 1 << (num - 1) > 0 else 0)
    elif operator == 'toggle':
        S = S ^ 1 << (num - 1)
    elif operator == 'all':
        S = (1 << 20) - 1
    else:
        S = 0