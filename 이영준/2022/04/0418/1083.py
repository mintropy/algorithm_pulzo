"""
Title : 소트
Link : https://www.acmicpc.net/problem/1083
"""

if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    sorted_seq = sorted(seq, reverse=True)
    S = int(input())
    for left in range(N):
        if S == 0:
            break
        if seq[left] == sorted_seq[left]:
            continue
        right = N
        while left < right:
            m = max(seq[left:right])
            m_idx = seq.index(m)
            if m_idx - left > S:
                right -= 1
                continue
            for k in range(m_idx, left, -1):
                seq[k], seq[k - 1] = seq[k - 1], seq[k]
            S -= m_idx - left
            break
    print(*seq)

'''
10
11 6 20 1 2 34 5 3 68 10
8
-> 68 11 6 20 1 2 34 5 3 10
'''
