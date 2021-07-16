from utils import generate_random_number, get_round_difficulty_level, verify_picked_number, lose_points


def play():
    print("Welcome to Guess the Number Game!")
    print("*********************************")

    MAX_NUMBER = 101
    MIN_NUMBER = 1

    hyper_secret_number = generate_random_number(MIN_NUMBER, MAX_NUMBER)
    max_tries = get_round_difficulty_level()
    total_tries = 1
    total_wins = 0
    total_points = 1000

    while total_tries <= max_tries:
        print("---------------------------------")

        print("Attempt {} of {}".format(total_tries, max_tries))

        picked_number = int(input("Type a number between 1 and 100 that you think is the right one: "))
        print("You choose", picked_number)

        is_right = verify_picked_number(picked_number, hyper_secret_number)

        if is_right:
            print("You guessed right and did {} points!".format(total_points))
            total_wins += 1
            break
        else:
            total_tries += 1
            total_points = lose_points(picked_number, hyper_secret_number, total_points)

    print("Game is over! \n")
    print("The hyper secret number was {}".format(hyper_secret_number))
    print("WINS: {}".format(total_wins))


if __name__ == "__main__":
    play()
