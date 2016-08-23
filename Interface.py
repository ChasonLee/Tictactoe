# -*- coding: utf-8 -*-
__author__ = 'Chason'

import pygame
from pygame.locals import *
from sys import exit
from math import *
from ChessBoard import ChessBoard
from StatisticAgent import StatisticAgent

base_size = 200

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

def draw_flag(screen, x, y, flag):
    if flag == 0:
        pygame.draw.arc(screen, (200,0,0), (x / base_size * base_size + 20, y / base_size * base_size + 20, base_size - 40, base_size - 40), 0, 180, 5)
    else:
        pygame.draw.line(screen, (0,100,200), (x / base_size * base_size + 40, y / base_size * base_size + 40),
                                            (x / base_size * base_size + base_size - 40 , y / base_size * base_size + base_size - 40), 10)
        pygame.draw.line(screen, (0,100,255), (x / base_size * base_size + base_size - 40 , y / base_size * base_size + 40),
                                            (x / base_size * base_size + 40, y / base_size * base_size + base_size - 40), 10)

def pygame_test():
    SCREEN_SIZE = (base_size * 3, base_size * 3)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
    while True:
        event = pygame.event.wait()
        screen.fill((0,0,0))
        if event.type == QUIT:
            exit()
        screen_width, screen_height = SCREEN_SIZE

        line_color = (100,200,100)
        pygame.draw.line(screen, line_color, (0, base_size), (screen_width, base_size), 5)
        pygame.draw.line(screen, line_color, (0, base_size * 2), (screen_width, base_size * 2), 5)
        pygame.draw.line(screen, line_color, (base_size, 0), (base_size, screen_height), 5)
        pygame.draw.line(screen, line_color, (base_size * 2, 0), (base_size * 2, screen_height), 5)

        pressed_mouse = pygame.mouse.get_pressed()
        if pressed_mouse[0]:
            x, y =  pygame.mouse.get_pos()
            print x,y
            draw_flag(screen, x, y, 0)
        elif pressed_mouse[2]:
            x, y =  pygame.mouse.get_pos()
            print x,y
            draw_flag(screen, x, y, 1)
        pygame.display.update()


# rnd_test()
# statistic_test()
pygame_test()
