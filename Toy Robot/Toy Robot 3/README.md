# Heading 1 Toy Robot 3

The project got expanded to keep track of a list of previos move commands and 
make a funcion called replay that when called with tags would replay the 
commands in history. 

The tags where reversed and silent. Silent replay the commands with out text 
output. Reversed replayed them in reverse order. The tags would work 
individually and together. Another tag was a range or intger. The range was from 
x to y in the list of commadns and the intger was jsut the last x commands.

The history function was easy as storing a list ofeach command and filtering out
the commands that wern't movement commands.

Replay was a bit harder but i itereated through the list and for each command i 
ran it throught its appropraite function. I also added booleans to check for the
tags and as each was raised. For each tag i either altereted the out put or the 
list of commands.

The range was by far the hardest task i had until i learnt i can control the 
start and end point of the list by passing the range values into it as the 
appropriate variables.