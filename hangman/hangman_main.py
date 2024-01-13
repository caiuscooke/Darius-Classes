from random import randint
from HangmanBoardPrint import HangMan


print("Welcome to Hangman!")

randomWordList = ["cheese", "food", "putt", "engineering",
                  "forceful", ]
randomWord = randomWordList[randint(0, len(randomWordList) - 1)]

gameBoard = []
gameOver = False

for eachLetter in randomWord:
    gameBoard.append("_")

print('Type a letter to make a guess. If you ever would like to give up, simply type "exit"')

print("".join(gameBoard))
userInput = input()
incorrectGuesses = 0
incorrectlyGuessedLetter = []


def check_game_over():
    if "_" not in gameBoard:
        return True
    else:
        print(" ".join(incorrectlyGuessedLetter))
        print(7 - incorrectGuesses, " wrong guesses left!")
        return False


def add_letter_to_game_board():
    for eachLetter in range(len(randomWord)):
        if userInput == randomWord[eachLetter]:
            gameBoard[eachLetter] = userInput


def handle_incorrect_guess(incorrectGuesses):
    if userInput not in randomWord:
        print("That letter is not in the word!")
        incorrectGuesses += 1

        if userInput not in incorrectlyGuessedLetter:
            incorrectlyGuessedLetter.append(userInput)
        else:
            print("You already guessed that letter!")

        return incorrectGuesses
    else:
        print("You got one!")
        add_letter_to_game_board()

        return incorrectGuesses


while gameOver == False:

    if userInput != "exit":
        incorrectGuesses = handle_incorrect_guess(incorrectGuesses)
        HangMan(incorrectGuesses)
        print("".join(gameBoard))
    else:
        break

    if incorrectGuesses == 7:
        print("Game Over! Better luck next time.")
        break

    gameOver = check_game_over()
    userInput = input()


if gameOver == True:
    print("Congratulations! You win!")
elif gameOver == False and incorrectGuesses != 7:
    print("Sorry to see you go!")
