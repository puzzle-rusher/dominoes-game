import random

import computer_turn_manager
from constants import *
from printer import print_state
from game_state_deducer import game_state
import player_turn_manager

def generate_all_pieces():
    result = []
    for i in range(0, 7):
        for j in range(i, 7):
            result.append([i, j])
    return result


def generate_sequences():
    pieces = generate_all_pieces()
    random.shuffle(pieces)
    return pieces[:14], pieces[14:21], pieces[21:]


def best_pair(pieces):
    max_pair = [-1, -1]
    for piece in pieces:
        if piece[0] == piece[1]:
            if max_pair[0] < piece[0]:
                max_pair = piece
    return max_pair


def generate_game():
    stock, computer, user = generate_sequences()
    computer_best_pair = best_pair(computer)
    user_best_pair = best_pair(user)

    if user_best_pair == [-1, -1] and computer_best_pair == [-1, -1]:
        return generate_game()
    else:
        if user_best_pair[0] < computer_best_pair[0]:
            computer.remove(computer_best_pair)
            return stock, computer, user, [computer_best_pair], PLAYER_TURN_STATUS
        else:
            user.remove(user_best_pair)
            return stock, computer, user, [user_best_pair], COMPUTER_TURN_STATUS


def play_game(stock, computer, user, snake, status):
    print_state(stock, computer, user, status_pair, status)
    if status == PLAYER_TURN_STATUS:
        is_left, index = player_turn_manager.make_turn(snake, user)
        if index == 0:
            if len(stock) > 0:
                user.append(stock.pop())
        else:
            if is_left:
                new_element = user.pop(index - 1)
                if snake[0][0] == new_element[1]:
                    snake.insert(0, new_element)
                else:
                    snake.insert(0, new_element[::-1])
            else:
                new_element = user.pop(index - 1)
                if snake[-1][1] == new_element[0]:
                    snake.append(new_element)
                else:
                    snake.append(new_element[::-1])

        new_status = game_state(user, computer, snake, status)
        play_game(stock, computer, user, snake, new_status)
    elif status == COMPUTER_TURN_STATUS:
        is_left, index = computer_turn_manager.make_turn(snake, computer)
        if index == 0:
            if len(stock) > 0:
                computer.append(stock.pop())
        else:
            new_element = computer.pop(index - 1)
            if is_left:
                if snake[0][0] == new_element[1]:
                    snake.insert(0, new_element)
                else:
                    snake.insert(0, new_element[::-1])
            else:
                if snake[-1][1] == new_element[0]:
                    snake.append(new_element)
                else:
                    snake.append(new_element[::-1])
        new_status = game_state(user, computer, snake, status)
        play_game(stock, computer, user, snake, new_status)


stock, computer, user, status_pair, status = generate_game()
play_game(stock, computer, user, status_pair, status)
