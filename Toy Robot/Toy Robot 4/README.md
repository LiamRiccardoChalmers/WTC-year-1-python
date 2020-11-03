# Heading 1 Toy Robot 4

This projects focus wsa on modules and packages. Mainly i had to make a new gui
that ran with turtle and was a graphical representation of the graph the robot 
could move on. Also functions that could generate obstacles and provide 
collision logice for those obstacles where to be added.

The first step i had was to seperate my funcstions that updated my postion into
a module called text and turtle respectively and find a way to switch between 
each with an argument vector passed on boot up. 

My solution was to move only show position, is position allowed and update 
position. As for switching between the 2 guis i learnt how to use importlib in 
python to typecast a string as a module/package and assing a variable to it so 
all i would need to do was the name of the gui to a list of accpetable gui and
keep the functions similar between modules and packages.

To create the obstacles i randomsied them with random and insured no obstacle 
could generate on (0,0) as that was the starting point for the robot. I added 
functions to check if the robots current destination and its path to that 
destination where blocked. 

I added a function to turtle to draw obstacles called boot up and i also used 
it to clean the globals i have i made a similar version of it in text.
