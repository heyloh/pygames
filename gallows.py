from utils import print_guessed_letters, create_displayed_word, print_hanged_person, check_if_completed_word, \
    get_random_hyper_secret_word


def play():
    print("**********************************")
    print("**** Welcome to Gallows Game! ****")
    print("**********************************")

    hyper_secret_word = get_random_hyper_secret_word()
    displayed_word = create_displayed_word(hyper_secret_word)
    hanged = False
    is_right = False
    total_fails = 0
    MAX_TRIES = 6

    while not hanged and not is_right:
        print("==================================================")
        picked_letter = input("Pick a letter you think exists in the secret word: \n\n")
        picked_letter = picked_letter.lower()

        if picked_letter in hyper_secret_word:
            index = 0
            for letter in hyper_secret_word:
                if letter == picked_letter:
                    displayed_word[index] = letter
                index += 1
        else:
            total_fails += 1

        if total_fails >= MAX_TRIES:
            hanged = True
            print("You lose!\nThe word was {}.".format(hyper_secret_word))

        is_right = check_if_completed_word(displayed_word)

        print_guessed_letters(displayed_word)
        print_hanged_person(total_fails)

        if is_right:
            print("You win!")


if __name__ == "__main__":
    play()
