#!/usr/bin/python
# -*- coding:utf-8 -*-

def get_board_state(s):
    if len(s) == 16:
        n = 4
    elif len(s) == 36:
        n = 6
    res = []
    for i in range(n):
        res.append([s[i + j * n] for j in range(n)])
    return res

def get_board_string(l):
    a = [l[x][y] for y in range(len(l)) for x in range(len(l))]
    return ''.join(a)

def make_move_normal(board_string, start, end):
    board_state = get_board_state(board_string)
    start_x, start_y = start
    end_x, end_y = end
    if board_state[end_x][end_y] != '.' \
            or start_x < 0 or start_y < 0 \
            or end_x < 0 or end_y < 0:
        return None
    else:
        if abs(end_x-start_x) <= 1 \
            and abs(end_y-start_y) <= 1:
            board_state[end_x][end_y] = board_state[start_x][start_y]
            board_state[start_x][start_y] = '.'
            return get_board_string(board_state)
        else:
            return None


if __name__ == '__main__':
    print(make_move_normal('xxxx........oooo', (0, 0), (0, 1)))
    # '.xxxx.......oooo'
    print(make_move_normal('xxxx........oooo', (0, 0), (2, 2)))
    # None