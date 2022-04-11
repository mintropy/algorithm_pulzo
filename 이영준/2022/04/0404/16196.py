"""
Title : 중국 신분증 번호
Link : https://www.acmicpc.net/problem/16196
"""

import sys

input = sys.stdin.readline


if __name__ == "__main__":
    personal_id = input().strip()

    for _ in range(int(input())):
        region = input().strip()
        if personal_id[:6] != region:
            continue
        month_check = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = (
            int(personal_id[6:10]),
            int(personal_id[10:12]),
            int(personal_id[12:14]),
        )
        if (not year % 4 and year % 100) or not year % 400:
            month_check[2] += 1
        if 1900 <= year <= 2011 and 1 <= month <= 12 and 1 <= day <= month_check[month]:
            check_code = int(personal_id[14:17])
            if check_code:
                code = 0
                power = 2
                for i in personal_id[:17][::-1]:
                    code += power * int(i)
                    power *= 2
                target = 10 if personal_id[17] == "X" else int(personal_id[17])
                if (target + code) % 11 == 1:
                    print("M" if check_code % 2 else "F")
                else:
                    print("I")
            else:
                print("I")
        else:
            print("I")
        break
    else:
        print("I")
