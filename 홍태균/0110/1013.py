'''
Contact

'''
import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    pattern = list(map(int,input().strip()))
    idx = 0
    p_len = len(pattern)

    while idx < p_len:
        # 1 분기
        # 1
        if pattern[idx]:
            # 1-1 분기 남은 길이가 2이상이고 그 2개가 00일때
            # 100
            if idx + 2 < p_len and pattern[idx + 1] == pattern[idx + 2] == 0:
                idx += 2

                # 1-1-1 뒤에 0이 더있는지 확인
                while idx + 1 < p_len and pattern[idx] == 0:
                    idx += 1
                
                # 이미 길이를 넘으면 끝
                # 100..0
                if idx == p_len:
                    ans = "NO"
                    break

                # 뒤에 1이 있는지 확인
                # 100..1
                if idx + 1 < p_len and pattern[idx] == 1:
                    idx += 1
                
                # 1-1-2 뒤에 1이 더있는지 확인
                # 100..1
                while idx + 1 <= p_len and pattern[idx] == 1:
                    # 1-1-2-1 뒤에 길이가 2가 더 있는지 확인
                    # 다음이 0이 있는 확인
                    # 100..1..10
                    if idx + 2 < p_len and pattern[idx + 1] == 0:
                        # 1-1-2-1-1 뒤에 또 0이 있는지 확인
                        # 다시 첫번째 패턴이 나올 수 있는경우
                        # 100..1..100 
                        if pattern[idx + 2] == 0:
                            break
                        # 1-1-2-1-2
                        # 뒤에 2번째 패턴인 경우 해당 1은 현재 패턴의 것
                        # 100..1..101
                        else:
                            idx += 1
                            break
                    # 1-1-2-2 뒤에 1이 더있는 경우
                    # 100..11..
                    idx += 1

            # 1-2 분기 1다음에 00이 아니면 패턴에 맞지 않음
            # NO
            else:
                ans = "NO"
                break

        # 2 분기
        # 0
        else:
            # 2-1 0다음에는 무조건 1이 와야한다.
            # 01
            if idx + 1 < p_len and pattern[idx + 1]:
                idx += 2
            # 2-2 
            # 00 NO
            else:
                ans = "NO"
                break

    # 무사히 다 돌면 
    # YES
    else:
        ans = 'YES'

    print(ans)


'''
1
011000101100111001

YES

1
01100010110011101
'''