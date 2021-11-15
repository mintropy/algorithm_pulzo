import sys

input = sys.stdin.readline

arr = input().strip()
origin_double_colon_index = arr.find('::')
arr = list(arr.split(':'))


def rule_one():
    for i in range(8):
        tmp = change_arr[i]
        if len(tmp) < 4:
            change_arr[i] = '0' * (4 - len(tmp)) + tmp


if origin_double_colon_index == -1:  # 더블 콜론 없는 것
    change_arr = arr[::]
    rule_one()

else:  # 더블 콜론 있는 것
    double_colon_index = arr.index('')
    change_arr = arr[:double_colon_index] + ['0000'] * (9 - len(arr))  # 규칙 2
    if double_colon_index + 1 <= 8:  # 뒤에 꺼
        change_arr.extend(arr[double_colon_index + 1:])
    rule_one()

print(':'.join(change_arr))

'''
1::2:3:4:5:6:7

1:2::3:4:5:6:7

1:2:3::4:5:6:7 

2001:db8:85a3::8a2e:370:7334


'''
