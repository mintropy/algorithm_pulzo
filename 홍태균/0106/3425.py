'''
고스택

'''
import sys
input = sys.stdin.readline

# 계산
def calculate(N,opers):
    gostack = [N]
    # 연산 수행
    for oper in opers:
        # 각 연산은 스택에 숫자가 있어야함.
        if oper == 'POP':
            if gostack == []:
                print('ERROR')
                return
            gostack.pop()
        elif oper == 'INV':
            if gostack == []:
                print('ERROR')
                return
            gostack[-1] *= -1
        elif oper == 'DUP':
            if gostack == []:
                print('ERROR')
                return
            gostack.append(gostack[-1])
        # 해당 연산 부터 숫자가 2개 이상이어야함.
        elif oper == 'SWP':
            if len(gostack) < 2:
                print('ERROR')
                return
            gostack[-1], gostack[-2] = gostack[-2], gostack[-1]
        # 덧셈, 뺄셈, 곱셈은 숫자 2개를 꺼내서 연산하고 그 숫자의 절댓값이 10^9 이하여야함
        elif oper == 'ADD':
            if len(gostack) < 2:
                print('ERROR')
                return
            b = gostack.pop()
            a = gostack.pop()
            gostack.append(a+b)
            if abs(gostack[-1]) > 10**9:
                print('ERROR')
                return
        elif oper == 'SUB':
            if len(gostack) < 2:
                print('ERROR')
                return
            b = gostack.pop()
            a = gostack.pop()
            gostack.append(a-b)
            if abs(gostack[-1]) > 10**9:
                print('ERROR')
                return
        elif oper == 'MUL':
            if len(gostack) < 2:
                print('ERROR')
                return
            b = gostack.pop()
            a = gostack.pop()
            gostack.append(a*b)
            if abs(gostack[-1]) > 10**9:
                print('ERROR')
                return
        # 나누기는 0으로 나누면 안되고
        # 부호가 다르면 답이 - 이고 아니면 +
        elif oper == 'DIV':
            if len(gostack) < 2:
                print('ERROR')
                return
            b = gostack.pop()
            a = gostack.pop()
            if b == 0:
                print('ERROR')
                return
            if (a < 0 and b > 0) or (a > 0 and b < 0):
                ans = -1
            else:
                ans = 1
            a = abs(a)
            b = abs(b)
            ans *= (a//b)
            gostack.append(ans)
        # 나머지 연산은 0으로 나누면 안되고
        # 피제수의 부호와 같게 답이 출력
        elif oper == 'MOD':
            if len(gostack) < 2:
                print('ERROR')
                return
            b = gostack.pop()
            a = gostack.pop()
            if b == 0:
                print('ERROR')
                return
            if a < 0:
                ans = -1
            else:
                ans = 1
            a = abs(a)
            b = abs(b)
            ans *= (a%b)
            gostack.append(ans)
        # 위의 연산이 아니라면 NUM
        # 그렇기 때문에 숫자면 빼내서 스택에 추가
        else:
            b = oper[4:]
            b = int(b)
            gostack.append(b)
    # 모든 연산을 한 뒤 숫자가 1개가 아니면 ERROR
    if len(gostack) == 1:
        print(gostack[-1])
    else:
        print('ERROR')

# 문제 수행
def sol():
    while 1:
        # 연산 담기
        opers = []
        while 1:
            oper = input().strip()
            # 연산이 END면 연산 수행
            if oper == 'END':
                break
            # QUIT 면 끝
            elif oper == 'QUIT':
                return
            opers.append(oper)
        T = int(input().strip())
        # 각 숫자만큼 연산 수행
        for _ in range(T):
            # 해당 숫자와 연산모음을 넘겨줌.
            N = int(input().strip())
            calculate(N,opers)
        # 띄어쓰기와 엔터 넘기기
        print()
        input()

sol()

'''
입력:
INV
NUM 600000000
INV
ADD
END
1
600000000

INV
NUM 600000000
SUB
END
1
600000000

QUIT


정답:
ERROR

ERROR


오답:
-1200000000
-1200000000


NUM 4
INV
DIV
END
1
13

INV
NUM 4
MOD
END
1
13

INV
NUM 4
INV
MOD
END
1
13

QUIT

MUL
END
1
3

SUB
END
1
3

QUIT


NUM -2
MOD
END
2
2
3

QUIT
'''