from turn_validation import validate_turn


def make_turn(snake, hand_dominos):
    # returns is_turn_left, domino_number
    try:
        turn = int(input())
        if turn == 0:
            return True, 0
        abs_turn = abs(turn)
        domino = hand_dominos[abs_turn - 1]
        is_left = turn < 0
        if validate_turn(snake, domino, is_left):
            return is_left, abs_turn
        else:
            print("Illegal move. Please try again.")
            return make_turn(snake, hand_dominos)
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")
        return make_turn(snake, hand_dominos)
