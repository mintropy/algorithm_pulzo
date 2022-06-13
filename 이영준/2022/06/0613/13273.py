"""
Title : 로마숫자
Link : https://www.acmicpc.net/problem/13273
"""

import re
from sys import stdin

input = stdin.readline


def arabic_to_rome(arabic: str) -> str:
    res = ""
    l = len(arabic)
    for idx, x in enumerate(arabic):
        if x == "4":
            if l - idx == 3:
                res += "CD"
            elif l - idx == 2:
                res += "XL"
            elif l - idx == 1:
                res += "IV"
        elif x == "9":
            if l - idx == 3:
                res += "CM"
            elif l - idx == 2:
                res += "XC"
            elif l - idx == 1:
                res += "IX"
        else:
            x = int(x)
            if 5 <= x <= 8:
                if l - idx == 3:
                    res += "D"
                elif l - idx == 2:
                    res += "L"
                elif l - idx == 1:
                    res += "V"
                x -= 5
            if l - idx == 4:
                res += "M" * x
            elif l - idx == 3:
                res += "C" * x
            elif l - idx == 2:
                res += "X" * x
            elif l - idx == 1:
                res += "I" * x
    return res


def rome_to_arabic(rome: str) -> str:
    res = []
    res.append(rome.count("M") - rome.count("CM"))
    if "CM" in rome:
        res.append(9)
    elif "CD" in rome:
        res.append(4)
    else:
        res.append(rome.count("D") * 5 + rome.count("C") - rome.count("XC"))
    if "XC" in rome:
        res.append(9)
    elif "XL" in rome:
        res.append(4)
    else:
        res.append(rome.count("L") * 5 + rome.count("X") - rome.count("IX"))
    if "IX" in rome:
        res.append(9)
    elif "IV" in rome:
        res.append(4)
    else:
        res.append(rome.count("V") * 5 + rome.count("I"))
    return get_num(res)


def get_num(num_list: list) -> int:
    res = 0
    for x in num_list:
        res *= 10
        res += x
    return res


if __name__ == "__main__":
    for _ in range(int(input())):
        num = input().strip()
        match = re.match("[0-9]*", num)
        if match.group(0) == num:
            print(arabic_to_rome(num))
        else:
            print(rome_to_arabic(num))
