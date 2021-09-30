import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def myfunc(S):
    st = []
    ans = []

    op_prior = {
        '*': 1, '+': 1, '-': 0
    }

    for s in S:
        if s == '(':
            st.append(s)
        elif s == ')':
            while len(st) > 0 and st[-1] != '(':
                ans.append(st.pop())
            st.pop()
        elif s in op_prior:
            sw = False
            while len(st) > 0:
                if st[-1] not in op_prior:
                    break
                if op_prior[st[-1]] > op_prior[s]:
                    break
                if s == '-' and st[-1] == '-':
                    st.pop()
                    sw = True
                    break
                ans.append(st.pop())
            if not sw:
                st.append(s)
        else:
            ans.append(s)

    while len(st) > 0:
        ans.append(st.pop())
    return ans


def cal(x, op, y=None):
    if op == '-':
        if x == 0:
            return 2
        elif x == 1:
            return 1
        else:
            return 0
    elif op == '+':
        if x == 0 and y == 0:
            return 0
        elif x == 1 and y == 0:
            return 1
        elif x == 0 and y == 1:
            return 1
        elif x == 1 and y == 1:
            return 1
        else:
            return 2
    else:
        if x == 2 and y == 2:
            return 2
        elif x == 1 and y == 1:
            return 1
        elif x == 2 and y == 1:
            return 1
        elif x == 1 and y == 2:
            return 1
        else:
            return 0


def solve(postfix, P, Q, R):
    d = {'P': P, 'Q': Q, 'R': R}
    ret = []
    for s in postfix:
        if s == '-':
            tmp = ret.pop()
            ret.append(cal(tmp, s))
        elif s in '*+':
            tmp1 = ret.pop()
            tmp2 = ret.pop()
            ret.append(cal(tmp1, s, tmp2))
        elif s in 'PQR':
            ret.append(d[s])
        else:
            ret.append(int(s))
    #print(ret, P, Q, R)
    return ret[-1]


*S, _ = map(lambda x: x.rstrip(), sys.stdin)

for s in S:
    postfix = myfunc(s)
    ans = 0
    print(postfix)
    for P in range(3):
        for Q in range(3):
            for R in range(3):
                if(solve(postfix, P, Q, R) == 2):
                    ans += 1
    print(ans)
