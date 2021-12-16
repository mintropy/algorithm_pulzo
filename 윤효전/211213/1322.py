import sys
input = sys.stdin.readline

X, K = map(int, input().split())

binary_X = list(bin(X)[2:])
binary_K = list(bin(K)[2:])

ans = []

i = len(binary_X)-1
j = len(binary_K)-1
while j >= 0:
    #print(i, j)
    #print(*ans[::-1], sep='')
    if i < 0:
        ans.append(binary_K[j])
        j -= 1
        continue

    if binary_X[i] == '1':
        ans.append('0')
        i -= 1
    else:
        ans.append(binary_K[j])
        i -= 1
        j -= 1
#print(*ans[::-1], sep='')
print(int(''.join(ans[::-1]), 2))