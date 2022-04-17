'''
소트

'''
import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int,input().split()))
S = int(input())

for _ in range(S):
    for i in range(N-1):
        if num_list[i] < num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            break
    else:
        break

print(*num_list)
