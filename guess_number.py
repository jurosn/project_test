import random

def guess_number():
    print("Welcome to the 'Guess the Number' game!")
    secret = random.randint(1,100)
    tries = 0

    while True:
        guess = int(input("Please enter a number between 1 and 100:\n"))
        tries += 1

        if guess < secret:
            print("Your guess is too low.")
        elif guess > secret:
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed the number!")
            print(f"It took you {tries} tries. The secret number was {secret}.")
            break

if __name__ == "__main__":
    guess_number()