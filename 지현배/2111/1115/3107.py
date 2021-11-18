def sol(ip):
    ret = ''
    cnt = 0
    idx = len(ip) - 1
    while idx >= 0:
        if ip[idx] != ':':
            ret = ip[idx] + ret
            cnt += 1
        else:
            ret = ':' + '0' * (4 - cnt) + ret
            cnt = 0
        idx -= 1
    return '0' * (4 - cnt) + ret


in_ipv6 = input().rstrip()
ans = ''
if '::' in in_ipv6:
    head, tail = in_ipv6.split('::')
    print(sol(head) + ':' + '0000:' * (8 - in_ipv6.count(':')) + sol(tail))

else:
    print(sol(in_ipv6))