# Abraham Lincoln
# 07 FEB 20XX
# Text-Based Game

def game():

    answer = input('Would you like to play a game today? (y/n)\n').lower()

    if answer in ['y', 'yes']:
        print('Welcome to my text-based game!')
        start = True
        # Create an empty list named inventory
        inventory = []
    else:
        print('Okay, we will play the game some other time.')
        print('Goodbye!')

    if start == True:
        print('Greetings, traveller! I see you are new to this part of the realm.')
        print('Welcome to the Kingdom of Pulaskor.')
        print('Here you will ')







game()