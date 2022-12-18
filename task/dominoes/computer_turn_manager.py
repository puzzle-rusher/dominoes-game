import random
from turn_validation import validate_turn


def make_turn(snake, hand_dominos):
    # returns is_turn_left, domino_number
    input()
    return generate_move(snake, hand_dominos)


def generate_move(snake, hand_dominos):
    scores = compute_scores(snake, hand_dominos)
    dominoes_scores = compute_dominoes_scores(hand_dominos, scores)
    return find_suitable_from(dominoes_scores, snake, hand_dominos)


def find_suitable_from(dominoes_scores, snake, hand_dominos):
    turn = find_best_turn(dominoes_scores)
    if turn == 0 and dominoes_scores[0] == 0:
        return True, 0

    if fits_left(hand_dominos[turn], snake):
        return True, turn + 1
    elif fits_right(hand_dominos[turn], snake):
        return False, turn + 1
    else:
        dominoes_scores[turn] = 0
        return find_suitable_from(dominoes_scores, snake, hand_dominos)


def fits_left(domino, snake):
    return domino[0] == snake[0][0] or domino[1] == snake[0][0]


def fits_right(domino, snake):
    return domino[0] == snake[-1][-1] or domino[1] == snake[-1][-1]


def compute_scores(snake, hand_dominos):
    result = {}
    for number in range(0, 7):
        result[number] = 0

    for domino in snake + hand_dominos:
        result[domino[0]] += 1
        result[domino[1]] += 1

    return result


def compute_dominoes_scores(hand_dominos, scores):
    result = []

    for domino in hand_dominos:
        result.append(scores[domino[0]] + scores[domino[1]])

    return result


def find_best_turn(dominoes_scores):
    index = 0
    for (score_index, score) in enumerate(dominoes_scores):
        if score > dominoes_scores[index]:
            index = score_index
    return index
