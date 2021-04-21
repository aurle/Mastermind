from random import choice

# This function compares the player's guess to the answer
def check_guess(guess):
    right = 0
    wrong = 0
    for i in range(len(target)):
        if guess[i] == target[i]:
            right += 1

    # They got them all correct, so no need to continue
    if right == len(target):
        return 1

    # They didn't get them all correct, but tell them how many they did.
    print ("Right Color Right Location", right)

    # For the ones that were not correct, were the colors correct but in the
    # wrong place, or were the colors wrong entirely?
    # To figure this out, count the number of each color in the guess and target
    guess_color_count = [0 for x in range(len(colors))]
    target_color_count = [0 for x in range(len(colors))]
    for i in range(len(guess)):
        for j in range(len(colors)):
            if guess[i] == colors[j]:
                guess_color_count[j] += 1
            if target[i] == colors[j]:
                target_color_count[j] += 1

    # Tally up the results
    for j in range(len(colors)):
        if guess_color_count[j] and target_color_count[j]:
            wrong += min(guess_color_count[j],target_color_count[j])

    wrong -= right

    # Show the results to the player
    print ("right Color, Wrong location", wrong)

# This function randomly creates the answer the player will try to guess
def create_target():
  for color in target:
    color = choice(colors)

# This function checks the guess the user entered to make sure it is valid
def verify_colors(guess):
    verified = 0
    for i in range(len(guess)):
        for j in range(len(colors)):
            if guess[i] == colors[j]:
                verified = verified + 1 

    if verified < 4:
        print ("Bad guess, Use format R Y G B")
        return 0
    else:
        return 1

def instructions():
  print (f"{name}, I have chosen four colors from the selection R Y G B")
  print ("The colors can be any combination, I may have even used the same")
  print ("color more than once. You will try to guess the colors by entering")
  print ("four colors and after each guess, I will tell you how you did.")

guesses = 9
colors = ['R','Y','B','G']
target = ['B','G','R','Y']

print ("Welcome to the game of Mastermind\n")

# This will open a field where the player can type their name
name = input('Hello! What is your name? ')

# Call the instructions function to print the instructions for the player
instructions()

print ("Can you guess the colors in", guesses, "guesses?")

# Generate the colors that the player will try to guess
create_target()

# Get the player's guess and check it until they run out of turns
for i in range(0,guesses):
    good_guess = False
    while not(good_guess):
        guess = input('Enter guess\n')
        # input reads in a string and this converts it to a list
        guess = guess.split()
        # verify the guess only has valid colors
        good_guess = verify_colors(guess)

    # Check the player's guess. If it is correct exit
    if check_guess(guess):
        break

# Show them what the answer was
print (f"The target was {target[0]} {target[1]} {target[2]} {target[3]}")
