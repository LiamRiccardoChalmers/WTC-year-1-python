#   Hangman 3
The scope expaned to hiding all but 1 letter of a word and allowing the user 
multiple guess while printing out the different states of the hanged man.

I expaned the code that hide 1 letter to do all but 1 and i insured it 
accounted for double occurences of letters.

The multiple guess are controlled by a while loop that ends when either the 
guess is correct or the number of guess reaches 0.

I use the number of guess left as an index for the hangman graphics which i 
store in a list and then ndex with the guess remaining to choose the correct 
graphic to print out in terminal.
