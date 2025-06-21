import random

# Variable: Store the secret number
secret_number = random.randint(1, 10)

# Loop: Give the user 3 chances to guess
for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt} - Guess a number between 1 and 10: "))
    
    # Conditional Statements
    if guess == secret_number:
        print("🎉 Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

# Final message if user fails to guess
if guess != secret_number:
    print(f"😞 Sorry, the number was {secret_number}. Better luck next time!")
