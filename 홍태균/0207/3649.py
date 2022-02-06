'''
로봇 프로젝트

'''
import sys
input = sys.stdin.readline

# 여러 테스트 케이스 받는 방법
while 1:
    try:
        x = int(input())
        # 단위 변경
        x = x * 10000000
        N = int(input())

        rego_list = []
        for _ in range(N):
            rego = int(input())
            rego_list.append(rego)

        rego_list.sort()
        
        # 투 포인터(앞과 뒤에서 각각 시작)
        one_pt = 0
        two_pt = N - 1
        # flag로 정답 유무 확인
        flag = False
        while one_pt < two_pt:
            # x와 길이가 같으면 flag를 true
            if rego_list[one_pt] + rego_list[two_pt] == x:
                flag = True
                break
            # 길이가 짧으면 앞의 포인터를 늘리면 길이가 늘어나기 때문에 늘려준다.
            elif rego_list[one_pt] + rego_list[two_pt] < x:
                one_pt += 1
            # 길이가 길다면 뒤의 포인터를 줄이면 길이가 줄어들기 때문에 줄인다.
            else:
                two_pt -= 1
        
        # 정답이 있으면 yes 아니면 danger
        if flag:
            print('yes',rego_list[one_pt],rego_list[two_pt])
        else:
            print('danger')
    except:
        break


'''
1
5
1
2
5000000
5000001
5000002

'''