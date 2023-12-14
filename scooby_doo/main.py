import os
from string import ascii_lowercase, ascii_uppercase
from typing import List, Dict

# get current working directory, aka what folder does python think we're using
cur_dir = os.getcwd()

# use the join method to append "scooby_doo" to the end of the current directory
cur_dir = os.path.join(cur_dir, "scooby_doo")

# change the current directory to this project's folder named scooby_doo
os.chdir(cur_dir)

# use a dictionary to keep track of the answers the user gives
# if a user gives a certain answer, add 1 to that characters name the answer aligns with
# the program finds the highest number at the end and prints out whatever the key is
results = {
    "Fred": 0,
    "Daphne": 0,
    "Velma": 0,
    "Shaggy": 0,
    "Scooby": 0
}


# I used type notation (the arrows and the colons) to define my functions so you can see what
# you'd normally see in a real world environment
# -> List[str] means it's returning a list of strings

def read_file(file_name: str) -> List[str]:

    # this opens a file of the file name and reads it ('r')
    # assigns an alias/variable to the opened file with the 'as file:'
    with open(f"{file_name}", "r") as file:

        # .readlines() is a function for files that returns a list of the lines
        l = file.readlines()

        # this is known as LIST COMPREHENSION, we'll go over this in detail
        # LIST COMPREHENSION aside, all I'm doing here is stripping the '\n' character
        # from the items in this list
        l = [line.rstrip("\n") for line in l]

    return l


def get_qa():
    questions = read_file("questions.txt")

    answers = read_file("answers.txt")
    for index in range(len(answers)):
        answer = answers[index].split(sep=",")
        answers[index] = answer

    q_a_dict = {}  # initializing a dictionary

    # enumerate is a class that allows you to get the index AND value of an iterable
    # and then loop over it
    for index, value in enumerate(questions):
        q_a_dict[value] = answers[index]

    return q_a_dict


def get_keys() -> List[Dict[str, str]]:
    keys = read_file("keys.txt")
    keys = [key.split(sep=",") for key in keys]
    for index, inner_list in enumerate(keys):
        new_dict = {}
        letters = ascii_lowercase[:len(inner_list)]
        for ind, item in enumerate(inner_list):
            letter = letters[ind]
            new_dict[letter] = item
        keys[index] = new_dict
    return keys


def increment_result(answer: str, question_number: int):
    keys = get_keys()
    current_question_key = keys[question_number]
    value = current_question_key[answer]
    if "and" not in value:
        results[value] += 1
    else:
        for name in results:
            if name in value:
                results[name] += 1


def main():
    print("Type a, b, c, etc. and hit enter to choose an answer:")

    question_number = 0
    for q, a in get_qa().items():
        print(q)
        letters = ascii_uppercase[:len(a)]
        for ind, option in enumerate(a):
            print(f'{letters[ind]}) {option}')
        user_answer = input().lower()
        while user_answer.upper() not in letters:
            print(
                "That is not a possible choice! Please type one of the letters next to the question")
            user_answer = input().lower()
        increment_result(user_answer, question_number)
        question_number += 1
        # print(results)
    result = max(results, key=results.get)
    print(f'\nYou are most like {result}!')


main()


"""
This was my first attempt
Realized it would take long time to write out like this, and it wasn't efficient.
What you see above was about an hour and a half of testing/trying different things
and using google/chat gpt! Don't get discouraged if you feel like you wouldn't have
been able to do this. We all start somewhere. 3 years ago this would've taken me 4
days.
"""


# def question(question_number, q_a_list, key_list):
#     print(f"Question {question_number}")
#     print(q_a_list[0])
#     print(f"A) {q_a_list[1]}")
#     print(f"B) {q_a_list[2]}")
#     print(f"C) {q_a_list[3]}")
#     print(f"D) {q_a_list[4]}")
#     answer = input().lower()

#     if answer == "a":
#         answer = key_list[0]
#     elif answer == "b":
#         answer = key_list[1]
#     elif answer == "c":
#         answer = key_list[2]
#     elif answer == "d":
#         answer = key_list[3]
#     elif len(key_list) > 4:
#         if answer == "f":
#             answer = key_list[4]

#     if type(answer) != tuple:
#         increment_result(answer)
#     else:
#         increment_result(answer[0])
#         increment_result(answer[1])
