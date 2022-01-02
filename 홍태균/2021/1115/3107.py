'''
IPv6

'''
import sys
input = sys.stdin.readline

# 마지막 \n을 제거하기 위해서
pre_address = input().strip()

# ::이 있으면 생략이 되어다는 것.
if '::' in pre_address:
    # 생략된 수는 ::가 있기 때문에 
    # 8에서 :수를 빼면 생략된 수를 알 수 있다.
    num = 8 - pre_address.count(':')
    # 생략된 부분을 위해서 0으로 넣고 추가
    in_address = ':' + '0:' * num
    # ::와 in_address로 바꾼다.
    pre_address = pre_address.replace('::',in_address)

result = ''
# :로 구분하고 각 생략된 부분을 위해서 
# zfill로 채운다
for i in pre_address.split(':'):
    result += i.zfill(4) + ':'

# 마지막 :을 제거하기 위해서
print(result[:-1])