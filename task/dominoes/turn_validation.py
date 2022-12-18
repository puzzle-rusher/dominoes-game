def validate_turn(snake, domino, is_left):
    number = snake[0 if is_left else -1][0 if is_left else -1]
    return domino_contains(number, domino)


def domino_contains(number, domino):
    return domino[0] == number or domino[1] == number
