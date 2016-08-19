# -*- coding: utf-8 -*-
__author__ = 'Chason'
init_board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

class ChessBoard:
    def __init__(self):
        self.board = init_board
        self.draw_flag = 0
        self.player1_flag = 1
        self.player2_flag = 2
        self.row = 3
        self.col = 3
        self.win_num = 3

    def judge(self, r, c):
        player = self.board[r][c]
        for i in range(4):
            if i == 0:
                dr = -1
                dc = -1
            elif i == 1:
                dr = -1
                dc = 0
            elif i == 2:
                dr = -1
                dc = 1
            else:
                dr = 0
                dc = 1
            nr = r + dr
            nc = c + dc
            count = 1
            while nr >= 0 and nr < self.row and nc >= 0 and nc < self.col:
                if self.board[nr][nc] == player:
                    count = count + 1
                    nr = nr + dr
                    nc = nc + dc
                else:
                    break
            dr = -dr
            dc = -dc
            nr = r + dr
            nc = c + dc
            while nr >= 0 and nr < self.row and nc >= 0 and nc < self.col:
                if self.board[nr][nc] == player:
                    count = count + 1
                    nr = nr + dr
                    nc = nc + dc
                else:
                    break
            if count >= self.win_num:
                return player

        return

    def print_board(self):
        for r in self.board:
            for c in r:
                print c,
            print
        print