
direction = {
    'LT': (-1, -1),
    'T': (0, -1),
    'RT': (1 ,-1),
    'R': (1, 0),
    'RB': (1, 1),
    'B': (0, 1),
    'LB': (-1, 1),
    'L': (-1, 0),
}

def nextLoc(loc, drct):
    return [loc[0] + direction[drct][0], loc[1] + direction[drct][1]]

def isOut(loc):
    if 0 <= loc[0] < 8 and 0 <= loc[1] < 8:
        return False
    else:
        return True

king, stone, N = input().split()
k_loc = [ord(king[0]) - ord('A'), 8 - int(king[1])]
s_loc = [ord(stone[0]) - ord('A'), 8 - int(stone[1])]
N = int(N)

for n in range(N):
    move = input()
    next_k_loc = nextLoc(k_loc, move)
    if (isOut(next_k_loc)):
        continue
    if (s_loc == next_k_loc):
        next_s_loc = nextLoc(s_loc, move)
        if (isOut(next_s_loc)):
            continue
        s_loc = next_s_loc
    k_loc = next_k_loc
last_king = chr(k_loc[0] + ord('A')) + str(8 - k_loc[1])
last_stone = chr(s_loc[0] + ord('A')) + str(8 - s_loc[1])
print(last_king, last_stone)