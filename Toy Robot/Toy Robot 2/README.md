# Heading 1 Toy robot 2
This project was similar to the toy robot interview question but with several 
key differences. 1 the robot will alwasys start at (0,0). 2 the co-ordinates
can be negative. 3 the robots 'table' is a graph from (-100, -200) to (100,200).

The first problem i faced was allowing the robot to tell the user what commands 
it understood as well as what each command did. I made a map that mapped a 
command onto a description as well as the functions system call.

The mapping onto the function system call allowed me to use the map to direct my
code to the appropriate commands to execute its code.

The next problem was its movement and keeping it within bounds as well as on the
correct direction of forward, back left and right. Keeping it in bounds was as 
simple as having each move function run a function to check if the move was 
within bounds before moving. 

The turning was harder but i solved that with another map that kept track of 
each direactions available turns from each direction as well as a varaible to 
adjust the axis its moving on.