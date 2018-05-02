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

def make_move_capture(board_string, start, end):
    if len(board_string) not in [16, 36] \
            or not isinstance(board_string, str) \
            or not isinstance(start, tuple) \
            or not isinstance(end, tuple) \
            or not isinstance(start[0], int) \
            or not isinstance(start[1], int) \
            or not isinstance(end[0], int) \
            or not isinstance(end[1], int) \
            or not len(start) == len(end) == 2:
        return None
    for bs in board_string:
        if bs not in ['o', 'x', '.']:
            return None

    board_state = get_board_state(board_string)
    start_x, start_y = start
    end_x, end_y = end
    if board_state[end_x][end_y] == '.' \
            or board_state[start_x][start_y] == board_state[end_x][end_y]\
            or start_x < 0 or start_y < 0 \
            or end_x < 0 or end_y < 0 \
            or start_x >= len(board_state) or start_y >= len(board_state) \
            or end_x >= len(board_state) or end_y >= len(board_state):
        return None
    else:
        n = len(board_state)
        board_flag = [[0 for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if board_state[x][y] == '.':
                    board_flag[x][y] = 1
        if auto_run(start, board_flag, end, n):
            board_state[end_x][end_y] = board_state[start_x][start_y]
            board_state[start_x][start_y] = '.'
            return get_board_string(board_state)
        else:
            return None

def auto_run(start, board_flag, end, n):
    next_locations, is_captured = next_step(start, board_flag, end, n)
    if is_captured:
        return True
    else:
        for ns in next_locations:
            board_flag[ns[0]][ns[1]] = 0
            if auto_run(ns, board_flag, end, n):
                return True

def next_step(now_location, board_flag, end, n):
    # n: 4 or 6
    x, y = now_location
    next_locations = []
    flag = True
    is_captured = False
    for i in range(x + 1, n):
        if board_flag[i][y] != 1:
            flag = False
            if end == (i, y):
                is_captured = True
            break
    if flag and n-1 != x:
        next_locations.append((n - 1, y))

    flag = True
    for i in range(x - 1, -1, -1):
        if board_flag[i][y] != 1:
            flag = False
            if end == (i, y):
                is_captured = True
            break
    if flag and 0 != x:
        next_locations.append((0, y))

    flag = True
    for j in range(y + 1, n):
        if board_flag[x][j] != 1:
            flag = False
            if end == (x, j):
                is_captured = True
            break
    if flag and n-1 != y:
        next_locations.append((x, n - 1))

    flag = True
    for j in range(y - 1, -1, -1):
        if board_flag[x][j] != 1:
            flag = False
            if end == (x, j):
                is_captured = True
            break
    if flag and 0 != y:
        next_locations.append((x, 0))

    circle_track = init_circle_track(n)
    if now_location in circle_track:
        next_locations.append(circle_track[now_location])
    next_locations = list(filter(lambda a: board_flag[a[0]][a[1]] == 1,
                                 next_locations))
    return next_locations, is_captured

def init_circle_track(n):
    if n == 4:
        tmp_dict = {}
        tmp_dict[(1, 0)] = (0, 1)
        tmp_dict[(0, 1)] = (1, 0)
        tmp_dict[(2, 0)] = (3, 1)
        tmp_dict[(3, 1)] = (2, 0)
        tmp_dict[(1, 3)] = (0, 2)
        tmp_dict[(0, 2)] = (1, 3)
        tmp_dict[(2, 3)] = (3, 2)
        tmp_dict[(3, 2)] = (2, 3)
        return tmp_dict

    if n == 6:
        tmp_dict = {}
        tmp_dict[(1, 0)] = (0, 1)
        tmp_dict[(0, 1)] = (1, 0)
        tmp_dict[(2, 0)] = (0, 2)
        tmp_dict[(0, 2)] = (2, 0)

        tmp_dict[(4, 0)] = (5, 1)
        tmp_dict[(5, 1)] = (4, 0)
        tmp_dict[(3, 0)] = (5, 2)
        tmp_dict[(5, 2)] = (3, 0)

        tmp_dict[(1, 5)] = (0, 4)
        tmp_dict[(0, 4)] = (1, 5)
        tmp_dict[(2, 5)] = (0, 3)
        tmp_dict[(0, 3)] = (2, 5)

        tmp_dict[(4, 5)] = (5, 4)
        tmp_dict[(5, 4)] = (4, 5)
        tmp_dict[(3, 5)] = (5, 3)
        tmp_dict[(5, 3)] = (3, 5)

        return tmp_dict


if __name__ == "__main__":
    print(make_move_capture('xxxx........oooo', (0, 0), (0, 1)))
    # None
    print(make_move_capture('x.xx.x......oooo', (1, 1), (1, 3)))
    # 'x.xx........oxoo'
