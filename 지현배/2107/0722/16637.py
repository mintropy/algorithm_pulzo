N = int(input())
expression = list(input())
result = float('-inf')

def addBracket(exp, idx):
    return exp[0:idx] + ['('] + exp[idx:idx + 3] + [')'] + exp[idx + 3:]

def calc(exp):
    idx = 0
    while len(exp) - 4 > idx:
        if exp[idx] != '(':
            idx += 1
            continue
        exp = exp[:idx] + [str(eval(''.join(exp[idx + 1: idx + 4])))] + exp[idx + 5:]
    idx = 0
    while len(exp) > 1:
        exp = [str(eval(''.join(exp[idx:idx + 3])))] + exp[idx + 3:]
    return int(exp[0])

def sol(exp, idx):
    if idx >= len(exp) - 1:
        global result
        result = max(result, calc(exp))
        return
    sol(addBracket(exp, idx), idx + 6)
    sol(exp, idx + 2)
sol(expression, 0)
print(result)