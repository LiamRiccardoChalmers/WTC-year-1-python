"""
a nested dictionary storing the directional values
a is y 
b is x
"""
cd = {
    "a":
    {
"left": "-b",
"right": "b"
    },

    "-a":
    {
"left": "b",
"right": "-b"
    },

 "-b":
    {
"left": "-a",
"right": "a"
    },

    "b":
    {
"left": "a",
"right": '-a'
    } 

}

def do_off(command, name, m, coml, position):
    """ 
    Prints the turning off message
    Get command actually terminates the program
    """
    print(name + ": Shutting down..")
    return (name + ": Shutting down..")


def do_help(command, name, m, coml, position):
    """
    prints out the command map in the formatiing it wants
    """
    x = ' ' * 4
    print('I can understand these commands:')
    str1 = ''
    for i in command:
       str1 += i.upper()+ x[len(i):] + ' - ' + command[i][0] + '\n'
    print(str1)
    return str1
    

def do_forward(command, name, number, position, m):
    """
    first runs a test to see if the move command is in range
    before it updates its postion it tells the user how far forward its moved
    if its true it will then run a function to update its position
    after updating its position it returns it 
    """
    a = False
    if m == "a" or m == 'b':
        a = check_range(position, number, m, 1)
    elif m == "-a" or m == '-b':
        a = check_range(position, number, m, -1)

    if a == True:
        print(' > ' + name + " moved forward by " + number + " steps.")
        #print(position)
        return do_location(name, command, number, position, m)

    else: 
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        print(f" > {name} now at position ({position[0]},{position[1]}).")
    return position

    
def do_back(command, name, number, position, m):
    """
    first runs a test to see if the move command is in range t he test varies based on its directional modifier m
    before it updates its postion it tells the user how far back its moved
    if its true it will then run a function to update its position
    after updating its position it returns it 
    """
    
    a = False
    if m == "a" or m == 'b':
        a = check_range(position, number, m, -1)
    elif m == "-a" or m == '-b':
        a = check_range(position, number, m, 1)
    
    if a == True:
        print(' > ' + name + " moved back by " + number + " steps.")
        #print(position)
        return do_location(name, command, number, position, m)

    else: 
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        print(f" > {name} now at position ({position[0]},{position[1]}).")
    return position


def do_location(name, command, number, position, m):
    """
    updates the x and y location based of the dircetional modifiy m
    it takes the x and y position as data stored in a tuple called position
    it reassings the new x and y values to the tuple called position
    it then prints out the current position
    """
    x =  position[0]
    y =  position[1]
    if m == 'a':
        if command == "forward":
            y =  int(number) + int(position[1])
        elif command == "back":
            y = (-1 * int(number) + int(position[1]))
        position = (int(x),int(y))
    elif m == '-a':
        if command == "forward":
            y =  (- 1 * int(number) + int(position[1]))
        elif command == "back":
            y =  (int(number) + int(position[1]))
        position = (int(x), int(y))
    
    elif m == 'b':
        if command == "forward":
            x =  int(number) + int(position[0])
        elif command == "back":
            x = -1 * int(number) + int(position[0])
        position = (int(x), int(y))
        
    elif m == '-b':
        if command == "forward":
            x =  -1 *int(number) + int(position[0])
        elif command == "back":
            x = int(number) + int(position[0])
        position = (int(x), int(y))

    print(f' > {name} now at position ({position[0]},{position[1]}).')

    return position


def do_right(command, name, m, coml, position):
    """
    modifies the m directional variable based of an input of right by just adjusting the value of m to the new apporpriate value 
    from the nested dictionary cd
    """
    print (" > " + name + " turned right.")
    m = cd[m][coml]
    print(f" > {name} now at position ({position[0]},{position[1]}).")
    return m


def do_left(command, name, m, coml, position):
    """
    modifies the m directional variable based of an input of left by just adjusting the value of m to the new apporpriate value 
    from the nested dictionary cd
    """
    print (" > " + name + " turned left.")
    m = cd[m][coml]
    print(f" > {name} now at position ({position[0]},{position[1]}).")
    return m


def check_range(position, number, m, n):
    """
    checks if adding the new distance it would move stored as number to its current x or y postion will exceed the boundaries
    the n value is the modifier if the movement is incrementing or decrementing the axis it is using
    """
    x = position[0] + (int(number)*n)
    y = position[1] + (int(number)*n)
    #print(position[0])
    if m == "b" or m == '-b':
        if x < 101  and x > -101:
            return True
        else:
            return False
    elif m == 'a' or m == '-a':

        if y < 201 and y > -201:
            return True
        else:
            return False
    return position


def check_range_sprint(position, number, m, n):

    """
    checks if adding the new sprint distance it would move stored as total run into a recursive functioin
    would exceed its current boundaries
    the n value is the modifier if the movement is incrementing or decrementing the axis it is using
    """
    number = total_rec(int(number), 0)
    x = position[0] + (int(number)*n)
    y = position[1] + (int(number)*n)
    #print(position[0])
    if m == "b" or m == '-b':
        if x < 101  and x > -101:
            return True
        else:
            return False
    elif m == 'a' or m == '-a':

        if y < 201 and y > -201:
            return True
        else:
            return False
    return position


def total_rec(number, total):
    """
    recursive function to find the total to check if the boundaries will be exceeded
    """
    if int(number) == 0:
        return total
    return total_rec(str((int(number)-1)), total + int(number))


def do_location_sprint(name, command, number, position, m, total):
    """
    updates the x and y location based of the dircetional modifiy m
    it gets it value total from a recursive function attached to sprint
    it takes the x and y position as data stored in a tuple called position
    it reassings the new x and y values to the tuple called position
    it then prints out the current position
    """
    x =  position[0]
    y =  position[1]

    if m == 'a':
            y =  1 *int(total) + int(position[1])
            position = (int(x), int(y))
    elif m == 'b':
            x =  1 *int(total) + int(position[0])
            position = (int(x), int(y))
    elif m == '-a':
            y =  -1 *int(total) + int(position[1])
            position = (int(x), int(y))
    elif m == '-b':
            x =  -1 *int(total) + int(position[1])
            position = (int(x), int(y))
    print(f' > {name} now at position ({position[0]},{position[1]}).')

    return position


def do_sprint(com, name, number, position, m):
    """
    takes a number and checks first if run through the recursive function if it exceeds the boundaries
    if not then  it runs the recursive function
    then using the return of the recursive function it updates its position
    """
    a = False
    if m == "a" or m == 'b':
        a = check_range_sprint(position, number, m, 1)
    elif m == "-a" or m == '-b':
        a = check_range_sprint(position, number, m, -1)

    if a == True:
        total = do_sprint_recursive(com, name, int(number), position, m, 0)
        return do_location_sprint(name, command, number, position, m, total)

    else: 
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        print(f" > {name} now at position ({position[0]},{position[1]}).")
    return position
    

def do_sprint_recursive(com, name, number, position, m, total):
    """
    recursive function to find the total distanced sprinted and print out each amount of steps sprinted
    """
    if int(number) == 0:
        return total
    print (f" > {name} moved forward by {number} steps.")
    return do_sprint_recursive(com, name, str(int(number)-1), position, m, total + int(number))


"""
map called command that stores all my commands and the details on what each does
"""
command = {
"off": ['Shut down robot', do_off],
"help": ['provide information about commands', do_help], 
"forward": ['moves robot forward by a set amount of steps then displays its postion', do_forward],
"back": ['moves robot back by a set amount of steps then displays its postion', do_back],
"right": ['turns the robot 90 degrees to the right', do_right],
"left" : ['turns the robot 90 degrees to the left', do_left],
"sprint" : ['makes the robot sprint forward', do_sprint]
}


def get_command(name):
    """
    function the runs the program
    it takes a user input and checks if falls into 2 types
    simple like help or off
    and complex like forward 10 and sprint 5
    based on the command it runs the apporpriate command from the dictionary command
    if the off command is entered it shuts down the program
    """
    global command
    position = (0,0)
    m = 'a'
    while 1:
        com = input(name + ": What must I do next? ").strip()
        comd = com
        coml = com.lower()
        if " " in  com:
            com,number = coml.split(" ")
            if com.lower() in command:
                #print("before ", position)
                position = command[com][1](com, name, number, position, m)
                #print("after ", position)
            else:
                
                print(name + ": Sorry, I did not understand '" + comd + "'.")
        elif coml in command and coml == "off":
            command[coml][1](command, name, m, coml, position)
            break
        elif coml in command:
            m = command[coml][1](command, name, m, coml, position) 
        else:
            print(name + ": Sorry, I did not understand '" + com + "'.")
    return coml


def get_name():
    """
    simple function to prompt user to name the robot and store the name
    the name is used in all manner off outputs to the
    """
    name = input("What do you want to name your robot? " )
    print(name + ": Hello kiddo!")
    return(name)

    
    
def robot_start():
    """This is the entry function, do not change"""
    com = ''
    name = get_name()
    while com != "off":
        com = get_command(name)


if __name__ == "__main__":
    robot_start()