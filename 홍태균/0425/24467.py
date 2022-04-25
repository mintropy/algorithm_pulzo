'''
혼자 하는 윷놀이

'''
import sys
input = sys.stdin.readline

now = 0
goal = 21
cnt = 10
flag_5 = False
goal_flag = False

while cnt:
    yut = input()
    
    zero_cnt = yut.count('0') 
    
    if zero_cnt == 0:
        now += 5
    elif zero_cnt == 4:
        now += zero_cnt
    else:
        now += zero_cnt
        cnt -= 1
    
    if now == 5:
        flag_5 = True
        goal = 17
    elif now == 8 and flag_5:
        goal = 12
    elif now == 10 and not flag_5:
        goal = 17
        
    if now >= goal:
        goal_flag = True
    
if goal_flag:
    print("WIN")
else:
    print("LOSE")
        