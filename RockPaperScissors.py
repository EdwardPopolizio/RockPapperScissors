import random  # Import random module to generate computer choice

# Define a list of valid choices
choices = ["Rock", "Paper", "Scissors"]

# Main game loop
while True:
    # Prompt the user for their choice
    user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # Generate a random choice for the computer
    computer_choice = random.choice(choices)

    # Display choices
    print(f"You chose {user_choice}. The computer chose {computer_choice}.")

    # Determine the result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("You lose!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
