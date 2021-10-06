import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    P, N = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) < P:
        print('IMPOSSIBLE')
    else:
        arr = sorted(list(enumerate(a)), key=lambda x: (x[1], -x[0]))
        answer = []
        paid = 0
        for i in range(N):
            if arr[i][1] < (P - paid) // (N - i):
                answer.append([arr[i][0], arr[i][1]])
                paid += arr[i][1]
            else:
                k = i
                while i < N:
                    answer.append([arr[i][0], (P - paid) // (N - k) + 1])
                    i += 1
                paid += ((P - paid) // (N - k) + 1) * (N - k)
                break
        while paid > P:
            answer[k][1] -= 1
            paid -= 1
            k += 1
        answer.sort()
        print(*list(map(lambda x: x[1], answer)))