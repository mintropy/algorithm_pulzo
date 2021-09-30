# import sys
# import itertools
# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# def make_comb(n):
#     comb_list = []
#     for i in range(1, n+1):
#         for v in itertools.combinations(range(n), i):
#             if chk_valid(v):
#                 comb_list.append(v)
#     return comb_list

# def chk_valid(l):
#     for a, b in zip(l, l[1:]):
#         if abs(a-b) == 1:
#             return False
#     return True

# def calc_all(s):
#     res = int(s[0])
#     for i in range(1, len(s), 2):
#         res = eval(f"{res}{''.join(s[i:i+2])}")
#     return res

# def calc_one(s, i):
#     res = s[::]
#     res[i*2:i*2+3] = ['(', str(eval(''.join(res[i*2:i*2+3]))), ')']
#     return res

# def del_brackets(s):
#     while '(' in s:
#         s.remove('(')
#     while ')' in s:
#         s.remove(')')

# _, S = input(), list(input().rstrip())
# res = calc_all(S)
# comb_list = make_comb(len(S)//2)
# for case in comb_list:
#     tmp = S[::]
#     for op_idx in case:
#         tmp = calc_one(tmp, op_idx)
#     del_brackets(tmp)
#     res = max(res, calc_all(tmp))
# print(res)

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