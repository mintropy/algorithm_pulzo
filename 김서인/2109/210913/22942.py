# 원의 중심 좌표 x 기준으로 정렬
# 옆에 있는 두 개 원씩 만나는지 보기
import sys

input = sys.stdin.readline

def is_meet(circle1, circle2):
    x1, r1 = circle1
    x2, r2 = circle2
    # if (x1 - x2) == 0 and r1 != r2: # 동심원
    #     return'Again'

    if (x1-x2)**2<(r1-r2)**2:
        return 'Again'
    if (r1 - r2) ** 2 <= (x1 - x2) ** 2 <= (r1 + r2) ** 2:
        return True
    return False


N = int(input())
circles = []
for _ in range(N):
    x, r = map(int, input().split())

    circles.append((x, r))

circles.sort()
def sol():
    for i in range(N - 1):
        circle1 = circles[i]
        circle2 = circles[i + 1]
        res = is_meet(circle1, circle2)

        if res == 'Again':
            j = i-1
            while j >= 0:
                circle3 = circles[j]
                res2 = is_meet(circle2, circle3)
                if res2 == 'Again':
                    j -= 1
                elif res2 == True:
                    return 'NO'
                elif res2 == False:
                    break

        elif res == True:
            return 'NO'
    return 'YES'
ans = sol()
print(ans)
