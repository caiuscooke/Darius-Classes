from random import randint
from typing import List


def assemble_game_board(word: str) -> List[str]:
    board = []
    for each_letter in word:
        board.append("_")
    return board


def get_guessed_letter():
    user_input = input()

    while type(user_input) != str:
        print("That is not a supported character. Please make sure to type in a letter.")
        user_input = user_input()

    user_input = user_input.lower()
    return user_input


def update_board(guessed_ltr: str, word: str, board: list) -> List[str]:

    for index, ltr in enumerate(word):
        if guessed_ltr == ltr:
            board[index] = guessed_ltr

    return board


def check_winner(board: list) -> bool:
    if "_" not in board:
        return True
    return False


def main():

    word_choices = ["cheese", "food", "putt", "engineering", "forceful", ]
    random_index = randint(0, len(word_choices) - 1)
    chosen_word = word_choices[random_index]

    game_board = assemble_game_board(chosen_word)

    incorrect_guesses_count = 0
    inccorectly_guessed_letters = ""

    print("Type in a letter to make a guess. If you'd like to quit, type 'exit'. Enjoy!")

    game_over = False

    while not game_over:
        guessed_letter = get_guessed_letter()

        if guessed_letter == "exit":
            print("Sorry to see you go!")
            break

        if guessed_letter in chosen_word:
            print("Nice! Got one right!")
            game_board = update_board(guessed_letter, chosen_word, game_board)
        else:
            print("Whoops! Got one wrong.\n\n")
            incorrect_guesses_count += 1
            inccorectly_guessed_letters += guessed_letter

        game_over = check_winner(game_board)

        if incorrect_guesses_count == 7:
            print("You lose!")
            print(f"The word was {chosen_word}")
            break

        if not game_over:
            print("Game Board...")
            print(" ".join(game_board) + "\n")

            print("Incorrectly Guessed Letters...")
            print(" ".join(inccorectly_guessed_letters), end="     ")

            print(f"Tries Remaining: {7 - incorrect_guesses_count}")
        else:
            print("You Win!")


if __name__ == '__main__':
    main()
