'''
0 만들기

'''
import sys
input = sys.stdin.readline

T = int(input().strip())

def dfs(N):
    # 시작은 1에서 부터
    stack = [(1,[])]

    while stack:
        now, opers = stack.pop()
        next = now + 1
        # 현재 N이라면 끝
        if now == N:
            # 연산과 숫자를 합치기 위해서 뒤에 하나 더 붙이기
            oper_list = list(opers) + ['']
            # 합치기
            res = "".join(i + j for i, j in zip(num_list, oper_list))
            # 계산 띄어쓰기 부분은 붙이기
            if eval(res.replace(" ","")) == 0:
                # 0이라면 결과에 넣기
                results.append(res)
            # 계속 탐색
            continue

        # 차례대로 넣기
        for oper in oper_lists:
            if oper == " ":
                stack.append((next,opers + [oper]))
            elif oper == "-":
                stack.append((next,opers + [oper]))
            else:
                stack.append((next,opers + [oper]))
                
for tc in range(1,T+1):
    N = int(input().strip())
    # ASCII 코드 순으로 하기위해서 
    oper_lists = ['-','+',' ']
    # 쓰는 숫자들
    num_list = list(map(str,range(1,N+1)))
    # 결과들 저장
    results = []

    # N을 넘겨준다
    dfs(N)

    # 결과들 출력
    for i in results:
        print(i)
    # 띄어쓰기
    print()

    # for oper_list in set(permutations(oper_lists,N-1)):
    #     oper_list = list(oper_list) + ['']
    #     res = "".join(i + j for i, j in zip(num_list, oper_list))
    #     print(res)
    #     if eval(res) == 0:
    #         print("#",res)
