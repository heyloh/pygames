from random import randrange


def generate_random_number(MIN_NUMBER, MAX_NUMBER):
    random_number = randrange(MIN_NUMBER, MAX_NUMBER)

    return random_number


def get_round_difficulty_level():
    print("Choose the difficulty for this round! It can be: \n (1) Easy \t (2) Medium \t (3) Hard")
    difficulty = int(input("Enter your choice: "))

    is_easy = difficulty == 1
    is_medium = difficulty == 2
    is_hard = difficulty == 3

    number_of_tries = 0

    if is_easy:
        number_of_tries = 20
    elif is_medium:
        number_of_tries = 10
    elif is_hard:
        number_of_tries = 3
    else:
        print("Please, choose a valid option.")
        return get_round_difficulty_level()

    return number_of_tries


def verify_picked_number(picked_number, hyper_secret_number):
    is_right_answer = picked_number == hyper_secret_number
    is_greater_number = picked_number > hyper_secret_number
    is_smaller_number = picked_number < hyper_secret_number

    is_right = False

    if is_right_answer:
        is_right = True
    else:
        if is_greater_number:
            print("Your number was greater...")
        elif is_smaller_number:
            print("Your number was smaller...")

        is_right = False

    return is_right


def lose_points(picked_number, hyper_secret_number, old_total_points):
    is_greater = picked_number > hyper_secret_number

    if is_greater:
        lost_points = picked_number - hyper_secret_number
    else:
        lost_points = hyper_secret_number - picked_number

    actual_total_points = old_total_points - lost_points

    return actual_total_points


def print_guessed_letters(displayed_word):
    print('\t'.join(str(letter.upper()) for letter in displayed_word))


def create_displayed_word(hyper_secret_word):
    displayed_word = ['_' for _ in hyper_secret_word]

    return displayed_word


def print_hanged_person(total_fails):
    if total_fails == 1:
        print("|---|   \n|   O   \n|       \n|       \n|       \n")
    elif total_fails == 2:
        print("|---|   \n|   O   \n|   |   \n|       \n|       \n")
    elif total_fails == 3:
        print("|---|   \n|   O   \n|  /|   \n|       \n|       \n")
    elif total_fails == 4:
        print("|---|   \n|   O   \n|  /|\  \n|       \n|       \n")
    elif total_fails == 5:
        print("|---|   \n|   O   \n|  /|\  \n|    \  \n|       \n")
    elif total_fails == 6:
        print("|---|   \n|   O   \n|  /|\  \n|  / \  \n|       \n")
    else:
        print("|---|   \n|       \n|       \n|       \n|       \n")


def check_if_completed_word(displayed_word):
    if "_" in displayed_word:
        return False
    else:
        return True


def get_random_hyper_secret_word():
    with open("secret_words.txt", "r") as words_file:
        words = [word.strip() for word in words_file]

    MAX_POSITION = len(words)
    MIN_POSITION = 0
    random_position = generate_random_number(MIN_POSITION, MAX_POSITION)

    random_word = words[random_position].lower()

    return random_word
