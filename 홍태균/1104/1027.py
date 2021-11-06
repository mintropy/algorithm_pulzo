'''
고층 건물

'''
import sys
input = sys.stdin.readline

N = int(input())

buildings = list(map(int,input().split()))

# 건물이 2개 이상일 때
if N != 1:
    # 건물이 2개 이상일 때 양끝의 건물은 바로 옆에 1개의 건물은 무조건 볼 수 있고
    # 가운데 건물의 경우 양쪽의 건물을 볼 수 있기 때문에 
    # 초기화를 1 2 ... 2 1 로 해준다. 
    ans_list = [1] + [2] * (N-2) + [1]

    # 앞 건물하나를 선택하고
    # 뒤의 건물을 하나씩 선택하며 사이의 건물이 가리는지 확인
    for i in range(N-2):
        for j in range(i+2,N):
            # 앞 건물과 뒤의 건물 옥상사이의 선을 연결
            # 두 점을 지나는 선분 구하는 식 ((x2-x1)*y + (y1-y2)*x + x1*y2 - x2*y1)
            line = [j-i,buildings[i]-buildings[j],i*buildings[j] - j*buildings[i]]

            # 사이의 건물을 보면서 
            # 옥상의 위치를 대입했을 때 0보다 크면 선 위에 있는거고 작으면 선 아래에 있는 것이다.
            for k in range(i+1,j):
                # 가운데의 건물 중 하나라도 선 위에 있다면 다음 건물 보기
                if line[0]*buildings[k] + line[1]*k + line[2] >= 0:
                    break
            # 만약 사이의 건물이 가리는게 없다면 
            # 서로 건물이 볼 수 있기 때문에 둘다 증가
            else:
                ans_list[i] += 1
                ans_list[j] += 1

    # 그 중 가장 큰 값 
    print(max(ans_list))
# 건물이 1개 이면 0 출력
else:
    print(0)