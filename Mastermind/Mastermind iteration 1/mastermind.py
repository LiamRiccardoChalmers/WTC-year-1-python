import random

def generate_code():

    code_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    code = []

    i = 0

    while i < 4:

        digit_index = random.randint(1, len(code_range) - 1)

        digit = code_range[digit_index]

        code.append(digit)
        i +=1
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

    return ''.join(code)

def get_guess():

    code_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    guess = input('Input 4 digit code: ')

    while guess.strip() == '' or not len(guess) == 4 or not guess.isnumeric() or not check_in_range(code_range, guess):

        print('Please enter exactly 4 digits.')

        guess = input('Input 4 digit code: ')

    return guess

def check_in_range(code_range, guess):

    for elem in guess:

        if not elem in code_range or elem == '0':

            return False

    return True

def compare_guess(guess, answer, turns):

    finished = False

    if guess == answer:

        compare_right_pos(guess, answer)

        compare_wrong_pos(guess, answer)

        print('Congratulations! You are a codebreaker!')

        print('The code was: ' + guess)

        finished = True

    else:

        compare_right_pos(guess, answer)

        compare_wrong_pos(guess, answer)

        turns -= 1

        print('Turns left:', turns)

    return finished, turns

    

def compare_wrong_pos(guess, answer):

    num = 0

    for elem, index in zip(guess, answer):

        if elem in answer and not elem == index:

            num += 1

    print('Number of correct digits not in correct place:', num)

def compare_right_pos(guess, answer):

    num = 0

    for elem, index in zip(guess, answer):

        if elem in answer and elem == index:

            num += 1

    print('Number of correct digits in correct place:    ', num)

def run_game():

    end_conditions = (False, 12)

    game_code = generate_code()

    while not end_conditions[0] == True and end_conditions[1] > 0:

        player_guess = get_guess()

        end_conditions = compare_guess(player_guess, game_code, end_conditions[1])

if __name__ == "__main__":

    run_game()