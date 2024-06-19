import random

options = ("rock", "paper", "scissors")

def print_score(user_score, computer_score):
    print(f"\nScores:\nUser: {user_score}\nComputer: {computer_score}\n")

def main():
    running = True
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")
   

    while running:
        player = None
        computer = random.choice(options)

        while player not in options:
            player = input("Enter a choice (rock, paper, scissors): ").lower()

        print(f"\nPlayer: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print_score(user_score, computer_score)

        if input("Play again? (y/n): ").lower() != "y":
            running = False

    print("\nThanks for playing!")
    print_score(user_score, computer_score)

if __name__ == "__main__":
    main()
