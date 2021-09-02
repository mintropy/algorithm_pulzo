import sys
input = sys.stdin.readline
T = int(input())
g = [1] * 1000001
# i의 배수에 i를 더한다.
for i in range(2, 1000001):
    for j in range(i, 1000001, i):
        g[j] += i
    g[i] += g[i - 1]
for _ in range(T):
    print(g[int(input())])

# 전투의 흔적...
# import sys
# input = sys.stdin.readline
# T = int(input())
# ts = [0] * T
# MAXX = 0
# for i in range(T):
#     ts[i] = int(input())
#     if MAXX < ts[i]: MAXX = ts[i]
# M = [0, 1] + [0] * MAXX
# SUMM = [0, 1] + [0] * MAXX
# for i in range(2, MAXX + 1):
#     for j in range(1, int(i ** 0.5) + 1):
#         if i % j == 0:
#             if j == i // j:
#                 M[i] += j
#             else:
#                 M[i] += j + i // j
#     SUMM[i] = SUMM[i - 1] + M[i]
# for t in ts:
#     print(SUMM[t])
# import sys
# input = sys.stdin.readline
# T = int(input())
# M = [0, 1] + [0] * 999999
# sum = [0, 1] + [0] * 999999
# prime = [2]
# quest = [0 for _ in range(T)]
# max = 0
# for i in range(T):
#     quest[i] = int(input())
#     if max < quest[i]: max = quest[i]
# for i in range(3, max + 100):
#     for j in prime:
#         if j > i ** 0.5:
#             prime.append(i)
#             break
#         if i % j == 0:
#             break
# idx = 0
# for i in range(2, max + 1):
#     if i == prime[idx]:
#         idx += 1
#         M[i] = 1 + i
#     else:
#         num = i
#         pf = []
#         M[i] = 1
#         for p in prime:
#             while True:
#                 if num % p == 0:
#                     pf.append(p)
#                     num //= p
#                 else: break
#             if num == 1: break
#         index = 0
#         cnt = 1
#         while index < len(pf) - 1:
#             if pf[index] == pf[index + 1]:
#                 cnt += 1
#             else:
#                 M[i] *= (pf[index] ** (cnt + 1) - 1) // (pf[index] - 1)
#                 cnt = 1
#             index += 1
#         if pf[-1] != pf[-2]:
#             M[i] *= (pf[-1] ** 2 - 1) // (pf[-1] - 1)
#         else:
#             M[i] *= (pf[-1] ** (cnt + 1) - 1) // (pf[-1] - 1)
#     sum[i] = sum[i - 1] + M[i]
# for q in quest:
#     print(sum[q])