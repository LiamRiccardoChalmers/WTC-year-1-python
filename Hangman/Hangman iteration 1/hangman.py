#TIP: use random.randint to get a random word from the list
import random

def read_file(file_name):
    #path = '/home/c4r16s5/problems/submission_001-hangman/short_words.txt'
    short_words_file = open(file_name, 'r')
    words = short_words_file.readlines()
    short_words_file.close()
    """
    TODO: Step 1 - open file and read lines as words
    """
    return words

def select_random_word(words):

    randword = random.randint(0, len(words)-1)
    word = words[randword]
    randletter = random.randint(0, len(word)-1)
    print ("Guess the word: " + word[:randletter] + '_' + word[randletter + 1:])
    """
    TODO: Step 2 - select random word from list of file
    """
    return word



def get_user_input():
    user_input = input('Guess the missing letter: ')
    """
    TODO: Step 3 - get user input for answer
    """
    return user_input


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

