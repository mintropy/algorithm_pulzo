import sys
input = sys.stdin.readline

X, K = map(int, input().split())
bin_X = bin(X)[2:]
bin_K = bin(K)[2:]
x_idx = len(bin_X) - 1
k_idx = len(bin_K) - 1
bin_ans = ''
for i in range(x_idx, -1, -1):
    if k_idx == -1:
        break
    if bin_X[i] == '1':
        bin_ans = '0' + bin_ans
    else:
        bin_ans = bin_K[k_idx] + bin_ans
        k_idx -= 1
bin_ans = bin_K[0:k_idx + 1] + bin_ans
print(int(bin_ans, 2))