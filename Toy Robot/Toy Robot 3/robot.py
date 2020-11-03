
# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'replay silent', 'replay reversed', 'replay reversed silent']
valid_move_commands = ['forward', 'back', 'right', 'left', 'sprint']


# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#list of previously stored commands
history = []

#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.

def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    replay_list = command.split(" ")
    if check_second_arg(command) == True: 
        return command.lower()
    if "replay" in command.lower() and command.lower() in valid_commands:
        return command.lower()
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
    create_history(command)
    return command.lower()


def check_second_arg(command):
    """
    checks the second argument in the replay command so that if its there its 
    a valid range or if its not there to proceed as normal
    Only returns true or false
    """
    replay_list = command.split(" ")
    a = ''
    b = ''
    for i,x in enumerate (replay_list):
        if i == 1:
            a = x
            pass
        else:
            b += x
    if "-" in a and b.lower() not in valid_move_commands:
        for x in a.split('-'):
            if x.isdigit() == False:
                return False
        return True
    elif a.isdigit() and b not in valid_move_commands:
        return True
    else:
        return False

def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    if 'replay' in command:
        return command.lower() in valid_commands
    else:
        (command_name, arg1) = split_command_input(command)

        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays the last x commands or commands in a range
SILENT - makes the replay function replay without showing its outputs
REVERSED - makes replay replay commands in the reversed order they appear
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def create_history(user_input):
    """
    function that stores each user input in a global variable called history
    only returns the history
    """
    global history
    history.append(user_input)
    return history

def do_replay(robot_name, user_input):
    """
    Command that replays all the previous commands after validatting they are 
    actualy movment commands in teh valid move commands list
    it then searches the replay command input for flags like silent or 
    reversed or both so that it can output a specific out put
    it returns the number of commands replayed and how they were replayed
    """
    global history, valid_move_commands

    history = list(filter(lambda x: x.split()[0] in valid_move_commands ,history))
    x = ''
    command_output = ''
    command_counter = 0
    command_list = ()
    replay_type = " commands."
    list_range = get_range(user_input, history)
    start = list_range[0]
    end = list_range[1]
    if 'silent' in user_input and 'reversed' in  user_input:
        command_list = history[::-1]
        replay_type = " commands in reverse silently."
    elif 'silent' in user_input:
        command_list = history
        replay_type = " commands silently."
    elif 'reversed' in user_input:
        command_list = history[::-1]
        replay_type = " commands in reverse."
    else:
        command_list = history

    for x in command_list[start:end]:
        if " " in x:
            command_name, arg = x.split(" ")
        else:
            command_name = x
        if command_name == 'forward':
            (do_next, command_output) = do_forward(robot_name, int(arg))
            command_counter += 1 
        elif command_name == 'back':
            (do_next, command_output) = do_back(robot_name, int(arg))
            command_counter += 1 
        elif command_name == 'right':
            (do_next, command_output) = do_right_turn(robot_name)
            command_counter += 1 
        elif command_name == 'left':
            (do_next, command_output) = do_left_turn(robot_name)
            command_counter += 1 
        elif command_name == 'sprint':
            (do_next, command_output) = do_sprint(robot_name, int(arg))
            command_counter += 1 
        if "silent" not in user_input:
            print(command_output)
            show_position(robot_name)
            x = ' > '+robot_name+' replayed '+str(command_counter) + replay_type
        else:
            x = ' > '+robot_name+' replayed '+str(command_counter) + replay_type
        
        
    return True, str(x)


def get_range(user_input, history):
    """
    function that takes the second arg of the replay command checks if it is 
    a range or integer to use to replay a set of commands once it validates 
    that it is it decides if its a range or a int and repoduces the correct variables
    for the for loop in the replay function to start and end on
    returns only start and end
    """
    args = user_input.split(' ')
    start = 0
    end = len(history)
    a = ''
    for i,x in enumerate(args):
        if i == 0:
            a = x
        else:
            pass
    if "-" in a:
        string_range = a.split('-')
        start = (int(string_range[1])-1)
        end = (int(string_range[0])-1)
        return start,end
    elif a.isdigit():
        start = len(history)- int(a) 
        end = len(history)
        return start,end
    else:
        pass 
    return start,end


def handle_command(robot_name, command, replay=False):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    command_output = " "
    do_next = True
    user_input = (command_name, arg) = split_command_input(command)
    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay':
        (do_next, command_output) = do_replay(robot_name, arg)

    print(command_output)
    show_position(robot_name)
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, history

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    history = []
    position_x = 0
    position_y = 0
    current_direction_index = 0

    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")
    


if __name__ == "__main__":
    robot_start()
