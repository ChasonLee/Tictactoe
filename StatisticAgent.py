# -*- coding: utf-8 -*-
__author__ = 'Chason'

import copy
from ChessBoard import ChessBoard

class StatisticAgent:
    def __init__(self, chess_board, my_flag, enemy_flag, sim_times = 1000):
        self.chess_board = chess_board
        self.my_flag = my_flag
        self.enemy_flag = enemy_flag
        self.sim_times = sim_times

    def simulation(self, r, c):
        sim_board = copy.deepcopy(self.chess_board.board)
        sim_chess_board = ChessBoard(sim_board)
        winner = sim_chess_board.make_a_move(r, c, self.my_flag)
        if winner == self.chess_board.draw_flag:
            return 0.0
        elif winner == self.my_flag:
            return 1.0
        win_times = 0
        for i in range(self.sim_times):
            sim_board2 = copy.deepcopy(sim_board)
            sim_chess_board2 = ChessBoard(sim_board2)
            while True:
                winner = sim_chess_board2.make_rnd_move(self.enemy_flag)
                if winner != None:
                    break
                winner = sim_chess_board2.make_rnd_move(self.my_flag)
                if winner == self.my_flag:
                    win_times += 1
                    break
                elif winner == self.chess_board.draw_flag:
                    break
        return 1.0 * win_times / self.sim_times

    def statistic_calculating(self):
        empty = self.chess_board.search_empty_spaces()
        scores = []
        for e in empty:
            print 'e =', e
            r, c = self.chess_board.line2matrix(e)
            scores.append(self.simulation(r, c))
        print scores
        max_score = 0
        max_score_inx = 0
        for i,s in enumerate(scores):
            if s >= max_score:
                max_score = s
                max_score_inx = empty[i]
        return self.chess_board.line2matrix(max_score_inx)

    def make_statistic_move(self, chess_board, flag):
        r, c = self.statistic_calculating()
        if r != -1 and c != -1:
            winner = chess_board.make_a_move(r, c, flag, True)
            return winner
        else:
            return -1