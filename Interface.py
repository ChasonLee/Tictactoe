# -*- coding: utf-8 -*-
__author__ = 'Chason'
# import pygame
from ChessBoard import ChessBoard
from StatisticAgent import StatisticAgent

def rnd_test():
    cb = ChessBoard()
    sa = StatisticAgent(cb, cb.player1_flag, cb.player2_flag)

    cb.print_board()
    for i in range(9):
        winner = cb.make_rnd_move(sa.my_flag)
        cb.print_board()
        if winner != None and winner != -1:
            print winner, "wins!"
            break
        elif winner == -1:
            print "The game is already over."
            break
        r, c = 0, 0
        while True:
            move = [int(i) for i in raw_input("your move:").split()]
            r, c = move[0], move[1]
            if cb.is_empty(r, c):
                break
            else:
                print "[%d, %d] is occupied! Try again."%(r, c)
        winner = cb.make_a_move(r, c, sa.enemy_flag, True)
        cb.print_board()
        if winner != None:
            print winner, "wins!"
            break

def statistic_test():
    cb = ChessBoard()
    sa = StatisticAgent(cb, cb.player1_flag, cb.player2_flag)
    cb.print_board()

    for i in range(9):
        winner = sa.make_statistic_move(cb, sa.my_flag)
        cb.print_board()
        if winner != None and winner != -1:
            print winner, "wins!"
            break
        elif winner == -1:
            print "The game is already over."
            break
        r, c = 0, 0
        while True:
            move = [int(i) for i in raw_input("your move:").split()]
            r, c = move[0], move[1]
            if cb.is_empty(r, c):
                break
            else:
                print "[%d, %d] is occupied! Try again."%(r, c)
        winner = cb.make_a_move(r, c, sa.enemy_flag, True)
        cb.print_board()
        if winner == cb.player1_flag or winner == cb.player2_flag:
            print winner, "wins!"
            break
        elif winner == cb.draw_flag:
            print "There is a draw."
            break

# rnd_test()
statistic_test()
