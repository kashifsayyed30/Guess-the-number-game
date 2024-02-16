import random
logo = """

   _____                       _   _            _   _                 _               _ 
  / ____|                     | | | |          | \ | |               | |             | |
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __| |
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| |
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |  |_|
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_)
                                                                                        
                                                                                        
"""
print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")
actual_number = random.randint(1,100)
game_level = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()

def play_game(attempts):
    game_over = False
    while not game_over:
        user_guess = int(input("Guess the Number: \n"))
        if user_guess == actual_number:
            print(f"You guessed it right. The actual number was: {actual_number}")
            game_over = True
        elif user_guess < actual_number:
            print ("Too low.")
            print ("Guess again.")
            attempts -= 1
            while attempts > 0:
                print(f"You have {attempts} attempts remaining to guess the number.")
                break
            if attempts == 0:
                print(f"You maxed out on number of attenpts. You loose!! The actual number was: {actual_number}")
                game_over = True
        else: 
            print ("Too high.")
            print ("Guess again.")
            attempts -= 1
            while attempts > 0:
                print(f"You have {attempts} attempts remaining to guess the number.")
                break
            if attempts == 0:
                print(f"You maxed out on number of attenpts. You loose!! The actual number was: {actual_number}")
                game_over = True
            
if game_level == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    easy_attempts = 10
    play_game(easy_attempts)
elif game_level == 'hard':
    print("You have 5 attempts remaining to guess the number.")
    hard_attempts = 5
    play_game(hard_attempts)
else:
    print("Your option was invalid, please try again.")

