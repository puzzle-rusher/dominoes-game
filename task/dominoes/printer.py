from constants import *


def print_state(stock, computer, user, snake, status):
    print("=" * 70)
    print("Stock size:", len(stock))
    print("Computer pieces:", len(computer))
    print()
    print_snake(snake)
    print()
    print("Your pieces:")
    for (index, piece) in enumerate(user):
        print(str(index + 1) + ":" + str(piece))

    print()
    if status == COMPUTER_TURN_STATUS:
        print("Status: Computer is about to make a move. Press Enter to continue...")
    elif status == PLAYER_TURN_STATUS:
        print("Status: It's your turn to make a move. Enter your command.")
    elif status == PLAYER_WON_STATUS:
        print("Status: The game is over. You won!")
    elif status == COMPUTER_WON_STATUS:
        print("Status: The game is over. The computer won!")
    elif status == DRAW_STATUS:
        print("Status: The game is over. It's a draw!")
    else:
        print("WTF")


def print_snake(snake):
    if len(snake) > 6:
        print_flattened_array(snake[:3])
        print("...", end="")
        print_flattened_array(snake[-3:])
    else:
        print_flattened_array(snake)
    print()


def print_flattened_array(array):
    for element in array:
        print(element, end="")
