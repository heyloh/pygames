import guess_the_number
import gallows

print("Welcome, what do you want to play? \n(1) Guess the Number\t(2) Gallows")

game = int(input("Enter your choice: "))

is_guess_the_number = game == 1
is_gallows = game == 2

print("---------------------------------")
if is_guess_the_number:
    guess_the_number.play()
elif is_gallows:
    gallows.play()
