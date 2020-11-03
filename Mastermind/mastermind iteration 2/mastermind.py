import random


def generate_code():
    """Function to generate the code

Its parameters are to generate the codes digits are in between 1 and 8 as well as the code contains no duplicates

It returns the code
"""
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

    #print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return(code)


def get_guess():
    """Function to get the user input as a guess

Its parameters are to check if the len of the guess is 4. Otherwise it will keep assking for user input

It returns the guess
"""
    guess = input("Input 4 digit code: ")
    while len(guess) != 4:
        print("Please enter exactly 4 digits.")
        guess = input("Input 4 digit code: ")
    
    return(guess)


def answer_right_postion(answer, code):
    """Function to check if numbers in the correct guesses are in the code in the correct place

Its parameters are the code and the user inputed answer

It returns 'a' the number of correct digits in the correct place
"""
    a = 0
    
    for i in range(len(answer)):
            if code[i] == int(answer[i]):
                a = a + 1
    print('Number of correct digits in correct place:     '+ str(a))
    return(a)



def answer_wrong_postion(answer, code):
    """Function check if the guess are correct but in the wrong place

Its parameters are the code and the user inputed answer

It returns 'b' the number off correct guess in the wrong place
"""
    b = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            pass
        elif int(answer[i]) in code:
            b = b + 1
    print('Number of correct digits not in correct place: '+str(b))
    return(b)


def run_game():

    """Function to run the game

    Its are the number of turns and if the answer is correct

    It returns nothing
    """
    code = generate_code()
    correct = False
    turns = 0
    while not correct and turns < 12:
        answer = get_guess()
        correct_digits_and_position = answer_right_postion(answer, code)
        correct_digits_only = answer_wrong_postion(answer, code)
        correct_digits_only + 0
        turns += 1

        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))

    print('The code was: '+str(code))


if __name__ == "__main__":
    run_game()