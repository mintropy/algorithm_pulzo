import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, S = map(int, input().split())
board = list(map(lambda x:list(x.rstrip()), sys.stdin))

def find_ground_highest_edge_pos(board):
    res = [-3000] * S
    for i in range(R):
        for j in range(S):
            if board[i][j] == '#' and res[j] == -3000:
                res[j] = i
    return res

def find_meteor_lowest_edges_pos(board):
    res = [-3000] * S
    for i in range(R-1, -1, -1):
        for j in range(S):
            if board[i][j] == 'X' and res[j] == -3000:
                res[j] = i
    return res

def calc_distances(ground_pos, meteor_pos):
    grp_pos = zip(ground_pos, meteor_pos)
    res = map(lambda x:x[0]-x[1], grp_pos)
    return res

def find_nearest_distance(distances_between):
    return min(distances_between)

def find_all_meteor_pos(board):
    res = []
    for i in range(R):
        for j in range(S):
            if board[i][j] == 'X':
                res.append((i, j))
    return res

def remove_meteor_pos_on_board(all_meteor_pos, board):
    for i, j in all_meteor_pos:
        board[i][j] = '.'

def rewrite_meteor_pos_on_board(all_meteor_pos, can_fall_step_cnt, board):
    for i, j in all_meteor_pos:
        board[i+can_fall_step_cnt][j] = 'X'

def list_to_str_for_board(board):
    return [''.join(v) for v in board]

ground_highest_edge_pos = find_ground_highest_edge_pos(board)
meteor_lowest_edges_pos = find_meteor_lowest_edges_pos(board)
distances_between = calc_distances(ground_highest_edge_pos, meteor_lowest_edges_pos)
can_fall_step_cnt = find_nearest_distance(distances_between) - 1
all_meteor_pos = find_all_meteor_pos(board)
remove_meteor_pos_on_board(all_meteor_pos, board)
rewrite_meteor_pos_on_board(all_meteor_pos, can_fall_step_cnt, board)
board = list_to_str_for_board(board)

print(*board, sep='\n')