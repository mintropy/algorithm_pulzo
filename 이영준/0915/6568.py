"""
Title : 귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다
Link : https://www.acmicpc.net/problem/6568
"""

import sys
input = sys.stdin.readline


while True:
    try:
        memory = [0] * 32
        # 메모리에 먼저 저장
        for i in range(32):
            memory[i] = int(input().strip(), 2)
        # 가산기, pc
        adder = 0
        pc = 0
        while True:
            cmd = memory[pc] // 32
            num = memory[pc] % 32
            pc = (pc + 1) % 32
            # 각 명령어
            # 메모리주소의 주소에 값 저장
            if cmd == 0:
                memory[num] = adder
            # 메모리 주소의 값 가져오기
            elif cmd == 1:
                adder = memory[num]
            # 가산기 값이 0이면 pc 바꾸기
            elif cmd == 2:
                if not adder:
                    pc = num
            # 아무 행동 ㄴㄴ
            elif cmd == 3:
                continue
            # 가산기 값 '1' 감소
            elif cmd == 4:
                adder = (adder - 1) % 256
            # 가산기 값 '1' 증가
            elif cmd == 5:
                adder = (adder + 1) % 256
            # pc값 변경
            elif cmd == 6:
                pc = num
            # 프로그램 종료
            elif cmd == 7:
                break
        print(bin(adder)[2:].zfill(8))
    except:
        break
