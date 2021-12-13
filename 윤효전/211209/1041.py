import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
S = tuple(map(int, input().split()))

# A B C D E F
# 0 1 2 3 4 5

pick_3 = [
    (0,1,2),
    (0,1,3),
    (0,2,4),
    (0,3,4),
    (1,2,5),
    (1,3,5),
    (2,4,5),
    (3,4,5),
]

pick_2 = [
    (0,1),
    (0,2),
    (0,3),
    (0,4),
    (1,2),
    (1,3),
    (2,4),
    (3,4),
    (1,5),
    (2,5),
    (3,5),
    (4,5),
]

min_value_1 = float('inf')
min_value_3 = float('inf')
min_value_2 = float('inf')

for v in pick_3:
    min_value_3 = min(min_value_3, sum(map(lambda x:S[x], v)))
    
for v in pick_2:
    min_value_2 = min(min_value_2, sum(map(lambda x:S[x], v)))
    
min_value_1 = min(S)

if N == 1:
    ans = sum(S) - max(S)
else:
    ans = (min_value_1 * (N-2)**2 * 5) + (min_value_1 * (N-2) * 4) + (min_value_3 * 4) + (min_value_2 * (N-1)) * 4 + (min_value_2 * (N-2)) * 4
    
print(ans)
