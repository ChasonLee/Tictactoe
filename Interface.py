# -*- coding: utf-8 -*-
__author__ = 'Chason'

import pygame
from pygame.locals import *
from sys import exit
from math import *
from ChessBoard import ChessBoard
from StatisticAgent import StatisticAgent
import time
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
def xy2rc(x, y):
    return y / base_size, x / base_size

def draw_flag_mouse(screen, x, y, flag):
    if flag == 1:
        pygame.draw.arc(screen, (200,0,0), (x / base_size * base_size + 20, y / base_size * base_size + 20, base_size - 40, base_size - 40), 0, 180, 5)
    else:
        pygame.draw.line(screen, (0,100,200), (x / base_size * base_size + 40, y / base_size * base_size + 40),
                                            (x / base_size * base_size + base_size - 40 , y / base_size * base_size + base_size - 40), 10)
        pygame.draw.line(screen, (0,100,255), (x / base_size * base_size + base_size - 40 , y / base_size * base_size + 40),
                                            (x / base_size * base_size + 40, y / base_size * base_size + base_size - 40), 10)

def draw_flag_board(screen, r, c, flag):
    if flag == 1:
        pygame.draw.arc(screen, (200,200,0), (c * base_size + 20, r * base_size + 20, base_size - 40, base_size - 40), 0, 180, 5)
    elif flag == 2:
        pygame.draw.line(screen, (0,150,250), (c * base_size + 40, r * base_size + 40),
                                            (c * base_size + base_size - 40 , r * base_size + base_size - 40), 10)
        pygame.draw.line(screen, (0,150,250), (c * base_size + base_size - 40 , r * base_size + 40),
                                            (c * base_size + 40, r * base_size + base_size - 40), 10)

def draw_chessboard(screen, chess_board):
    for r_inx, r in enumerate(chess_board.board):
        for c_inx, c in enumerate(r):
            draw_flag_board(screen, r_inx, c_inx, c)

def pygame_test():
    SCREEN_SIZE = (base_size * 3, base_size * 3)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
    while True:
        event = pygame.event.wait()
        # screen.fill((0,0,0))
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
            draw_flag_mouse(screen, x, y, 1)
        elif pressed_mouse[2]:
            x, y =  pygame.mouse.get_pos()
            print x,y
            draw_flag_mouse(screen, x, y, 2)
        pygame.display.update()

def draw_background(screen, line_color, screen_width, screen_height):
    pygame.draw.line(screen, line_color, (0, base_size), (screen_width, base_size), 5)
    pygame.draw.line(screen, line_color, (0, base_size * 2), (screen_width, base_size * 2), 5)
    pygame.draw.line(screen, line_color, (base_size, 0), (base_size, screen_height), 5)
    pygame.draw.line(screen, line_color, (base_size * 2, 0), (base_size * 2, screen_height), 5)

def rnd_game():
    SCREEN_SIZE = (base_size * 3, base_size * 3)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

    cb = ChessBoard()
    sa = StatisticAgent(cb, cb.player1_flag, cb.player2_flag)

    draw_background(screen, (100,200,100), SCREEN_SIZE[0], SCREEN_SIZE[1])

    finished = False
    game_step = 0

    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            exit()
        pressed_mouse = pygame.mouse.get_pressed()
        if pressed_mouse[0] and game_step % 2 + 1 == sa.enemy_flag and finished == False:
            x, y =  pygame.mouse.get_pos()
            r, c = xy2rc(x, y)
            if cb.is_empty(r, c):
                winner = cb.make_a_move(r, c, sa.enemy_flag, True)
                game_step += 1
                draw_chessboard(screen, cb)
                if winner != None:
                    finished = True
        if (game_step % 2) + 1 == sa.my_flag and finished == False:
            winner = cb.make_rnd_move(sa.my_flag)
            game_step += 1
            draw_chessboard(screen, cb)
            if winner != None:
                finished = True

        pygame.display.update()

def game_setup():
    pass

def statistic_game():
    SCREEN_SIZE = (base_size * 3, base_size * 3)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
    background_color = (50,100,20)
    screen.fill(background_color)

    cb = ChessBoard()
    # pygame.draw.rect(screen, (50, 150, 100), Rect((100, 100), (400, 200)))
    button_color = (100, 250, 150)
    button1_rect = (100, 100, 400, 150)
    button2_rect = (100, 350, 400, 150)
    pygame.draw.ellipse(screen, button_color, button1_rect)
    pygame.draw.ellipse(screen, button_color, button2_rect)

    button1_text = "Player plays first"
    button1_font = pygame.font.SysFont("arial", 30)
    name_surface = button1_font.render(button1_text, True, (200, 100, 222), button_color)
    screen.blit(name_surface, (190, 150))

    button2_text = "AI plays first"
    button2_font = pygame.font.SysFont("arial", 30)
    name_surface = button2_font.render(button2_text, True, (200, 100, 222), button_color)
    screen.blit(name_surface, (220, 400))

    AI_plays_first = True
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            exit()
        pressed_mouse = pygame.mouse.get_pressed()
        if pressed_mouse[0]:
            x, y =  pygame.mouse.get_pos()
            if button1_rect[0] < x < button1_rect[0] + button1_rect[2] and button1_rect[1] < y < button1_rect[1] + button1_rect[3]:
                AI_plays_first = False
                time.sleep(0.5)
                break
            elif button2_rect[0] < x < button2_rect[0] + button2_rect[2] and button2_rect[1] < y < button2_rect[1] + button2_rect[3]:
                AI_plays_first = True
                time.sleep(0.5)
                break
        pygame.display.update()
    if AI_plays_first:
        sa = StatisticAgent(cb, cb.player1_flag, cb.player2_flag, 100)
    else:
        sa = StatisticAgent(cb, cb.player2_flag, cb.player1_flag, 100)

    screen.fill(background_color)

    draw_background(screen, (100,200,100), SCREEN_SIZE[0], SCREEN_SIZE[1])
    pygame.display.update()
    finished = False
    game_step = 0

    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            exit()
        pressed_mouse = pygame.mouse.get_pressed()
        if pressed_mouse[0] and game_step % 2 + 1 == sa.enemy_flag and finished == False:
            x, y =  pygame.mouse.get_pos()
            r, c = xy2rc(x, y)
            if cb.is_empty(r, c):
                winner = cb.make_a_move(r, c, sa.enemy_flag, False, True)
                game_step += 1
                draw_chessboard(screen, cb)
                if winner != None:
                    finished = True
                pygame.display.update()
        if (game_step % 2) + 1 == sa.my_flag and finished == False:
            winner = sa.make_statistic_move(cb, sa.my_flag)
            game_step += 1
            draw_chessboard(screen, cb)
            if winner != None:
                finished = True
            pygame.display.update()
        if finished == True:
            time.sleep(1)
            if pressed_mouse[0]:
                cb = ChessBoard()
                screen.fill(background_color)
                draw_background(screen, (100,200,100), SCREEN_SIZE[0], SCREEN_SIZE[1])
                pygame.display.update()
                finished = False
                game_step = 0
                if AI_plays_first:
                    sa = StatisticAgent(cb, cb.player1_flag, cb.player2_flag, 100)
                else:
                    sa = StatisticAgent(cb, cb.player2_flag, cb.player1_flag, 100)
# rnd_test()
# statistic_test()
# pygame_test()
# rnd_game()
statistic_game()