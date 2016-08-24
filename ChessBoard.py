# -*- coding: utf-8 -*-
__author__ = 'Chason'
from random import random

class ChessBoard:
    def __init__(self, board = None):
        if board == None:
            self.board = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]
        else:
            self.board = board
        self.draw_flag = 0
        self.player1_flag = 1
        self.player2_flag = 2
        self.row = 3
        self.col = 3
        self.win_num = 3

    def reset_board(self, board):
        self.board = board

    def is_empty(self, r, c):
        if self.board[r][c] == 0:
            return True
        else:
            return False

    def search_empty_spaces(self):
        inx = 0
        empty = []
        for r in self.board:
            for c in r:
                if c == 0:
                    empty.append(inx)
                inx += 1
        return empty

    def judge(self, r, c, print_judge = False):
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
                if print_judge:
                    print "player %d wins!"%player
                return player
        empty = self.search_empty_spaces()
        if empty == []:
            if print_judge:
                print "There is a draw."
            return self.draw_flag
        else:
            return None

    def print_board(self):
        for r in self.board:
            for c in r:
                print c,
            print
        print

    def make_a_move(self, r, c, flag, print_log = False, print_judge = False):
        self.board[r][c] = flag
        winner = self.judge(r, c, print_judge)
        if print_log:
            print "%d moved [%d, %d]"%(flag, r, c)
        return winner

    def line2matrix(self, num):
        r = num / self.col
        c = num % self.col
        return r, c

    def rnd_move(self):
        empty = self.search_empty_spaces()
        empty_count = len(empty)
        if empty_count > 0:
            rnd = (int)(random()*empty_count)
            return self.line2matrix(empty[rnd])
        else:
            return -1, -1

    def make_rnd_move(self, flag):
        r, c = self.rnd_move()
        if r != -1 and c != -1:
            self.board[r][c] = flag
            winner = self.judge(r, c)
            return winner
        else:
            return -1