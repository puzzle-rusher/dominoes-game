from constants import *

def game_state(player_stock, computer_stock, snake, last_state):
    if last_state == COMPUTER_TURN_STATUS and len(computer_stock) == 0:
        return COMPUTER_WON_STATUS
    elif last_state == PLAYER_TURN_STATUS and len(player_stock) == 0:
        return PLAYER_WON_STATUS
    else:
        if is_draw_game(snake):
            return DRAW_STATUS
        elif last_state == PLAYER_TURN_STATUS:
            return COMPUTER_TURN_STATUS
        else:
            return PLAYER_TURN_STATUS


def is_draw_game(snake):
    return len(snake) > 7 and snake[0][0] == snake[-1][-1] and count_the_number(snake[0][0], snake)


def count_the_number(dots, snake):
    count = 0
    for domino in snake:
        if domino[0] == dots:
            count += 1
        if domino[1] == dots:
            count += 1
    return count
