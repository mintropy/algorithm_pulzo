import sys
'''
9
5 1 6 2 9 8 4 7 2
'''

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
A_len = len(A)

max_length = 1
sibas = {0:[[]], 1:[[A[-1]]]}

for idx in range(A_len - 2, -1, -1):
    number = A[idx]
    target_len = max_length
    while target_len > 0:
        siba = sibas[target_len]
        isChange = False
        for sib in siba:
            if sib[-1] > number:
                if target_len == max_length:
                    isChange = True
                if target_len + 1 in sibas:
                    sibas[target_len + 1].append(sib + [number])
                else:
                    sibas[target_len + 1] = [sib + [number]]
                break
        if isChange == False:
            target_len -= 1
        else:
            max_length += 1
            break
    else:
        sibas[1].append([number])
    # print(sibas)
print(max_length)