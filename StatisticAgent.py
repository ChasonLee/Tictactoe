# -*- coding: utf-8 -*-
__author__ = 'Chason'
from random import random
import copy

class StatisticAgent:
    def __init__(self, chess_board, my_flag, enemy_flag):
        self.chess_board = chess_board
        self.my_flag = my_flag
        self.enemy_flag = enemy_flag
        self.sim_times = 10000

    def line2matrix(self, num):
        r = num / self.chess_board.col
        c = num % self.chess_board.col
        return r, c

    def search_empty_spaces(self, board):
        inx = 0
        empty = []
        for r in board:
            for c in r:
                if c == 0:
                    empty.append(inx)
                inx += 1
        return empty

    def rnd_move(self, board):
        empty = self.search_empty_spaces(board)
        empty_count = len(empty)
        if empty_count > 0:
            rnd = (int)(random()*empty_count)
            return self.line2matrix(empty[rnd])
        else:
            return -1, -1

    def make_rnd_move(self, board, flag):
        r, c = self.rnd_move(board)
        if r != -1 and c != -1:
            board[r][c] = flag
            winner = self.chess_board.judge(r, c)
            return winner
        else:
            return -1

    def make_a_move(self, board, r, c, flag):
        board[r][c] = flag
        winner = self.chess_board.judge(r, c)
        return winner

    def simulation(self, r, c):
        sim_board = copy.deepcopy(self.chess_board.board)
        self.make_a_move(sim_board, r, c, self.my_flag)
        for i in range(self.sim_times):
            sim_board2 = copy.deepcopy(sim_board)
            while True:
                winner = self.make_rnd_move(sim_board2, self.enemy_flag)
                if winner != None:
                    if winner == self.my_flag:
                        break
                winner = self.make_rnd_move(sim_board2, self.my_flag)
                if winner != None:
                    break


    def statistic_move(self):
        empty = self.search_empty_spaces(self.chess_board.board)
        scores = []
        for e in empty:
            r, c = self.line2matrix(e)
            scores.append(self.simulation(r, c))

