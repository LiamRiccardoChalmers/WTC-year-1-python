#   Mastermind 1
The scope was to build a basic version of the mastermind game the gode generated
code not have duplicate numbers nor the numbers 0 or 9 in it. Aside from that it
ran like a normal mastermind game.

My first step was to make a randomly generated code that did not have 
duplicates or the number 0 and 9 in it. After that i stored the code as an
imutable tuple

The next step was to while i ran my loop compare a guess from my user that i had
to check was a sequence of 4 numbers not including 0 and 9 to the code i 
generated. To do this i compared each number in the user input to the code at 
the same index. I did something similar for if it was the right digit in the 
wrong place.

THe games loop only ended after the user guessed correctly or ran out of guess.