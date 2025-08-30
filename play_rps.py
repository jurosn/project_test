import random

def play_rps():
    print("Welcome to Rock–Paper–Scissors!")
    choice = ['rock', 'paper', 'scissors']

    player_score = 0
    computer_score = 0

    rulers = {
        "rock":"scissors",
        "scissors":"paper",
        "paper":"rock"
    }

    while True:
        print("Enter 'q' to quit.")
        player = input("Choose 'rock', 'paper', 'scissors', 'q':\n")
        computer = random.choice(choice)
        print(f"Computer chose {computer}")

        if player == 'q':
            print(f"Your score is {player_score},\
                  computer score is {computer_score}")
            break

        if player not in choice:
            print("Invalid input. Please try again!")
            continue

        if player == computer:
            print("It's a tie.")
        elif rulers[player] == computer:
            print("You win!\n")
            player_score += 1
        else:
            print("You lose!\n")
            computer_score += 1

if __name__ == "__main__":
    play_rps()