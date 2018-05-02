#!/usr/bin/python
# -*- coding:utf-8 -*-

from capture_move import make_move_capture
from normal_move import make_move_normal

def make_move_sequence(board_string, move_sequence):
    for ms in move_sequence:
        n = make_move_normal(board_string, ms[0], ms[1])
        if n != None:
            board_string = n
            continue
        c = make_move_capture(board_string, ms[0], ms[1])
        if c != None:
            board_string = c
            continue
        return None
    return board_string

if __name__ == '__main__':

    print(make_move_sequence('xxxx........oooo', [((1, 0), (1, 1)), ((2, 3), (1, 2))]))
    # 'x.xx.x...o..oo.o'
    print(make_move_sequence('x.xx.x...o..oo.o', [((1, 2), (2, 1)), ((1, 1), (1, 3))]))
    # 'x.xx..o.....ox.o'