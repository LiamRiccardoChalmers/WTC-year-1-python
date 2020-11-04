import world.obstacles

#variables tracking position
position_x = 0
position_y = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

def boot_up(ob):
    """Function to boot up the gui for the different worlds

    Args:
        ob ([list]): [list of obstacles to initialise them in the gui]
    """
    global position_x, position_y
    position_x = 0
    position_y = 0

def show_position(robot_name, direction):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def check_blocked(new_x, new_y):
    """Function to check if my robot will hit an obstacle. If the returns are false
    return False if the path or final postion is blocked.

    Args:
        new_x ([int]): [the final x postion for a move command]
        new_y ([int]): [the final y postion for a move command]

    Returns:
        [boolean]: [true or false depending on the path or positong being blocked]
    """
    position = world.obstacles.is_position_blocked(new_x, new_y)
    path = world.obstacles.is_path_blocked(position_x, position_y, new_x, new_y)
    if position != True and path != True:
        return True
    else:
        return False


def update_position(steps,directions):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions == 'forward':
        new_y = new_y + steps
    elif directions == 'right':
        new_x = new_x + steps
    elif directions == 'back':
        new_y = new_y - steps
    elif directions == 'left':
        new_x = new_x - steps
    if check_blocked(new_x, new_y) == False:
        return False, ''
    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True, ''
    return False, 'boundary'
