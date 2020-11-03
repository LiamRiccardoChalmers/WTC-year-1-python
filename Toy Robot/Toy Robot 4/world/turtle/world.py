import turtle
import world.obstacles

#variables tracking position
position_x = 0
position_y = 0

#area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#turtle position
previous_direction = 'forward'

#turtle and turtle screen gets created
robot = turtle.Turtle()
screen = turtle.Screen()

def boot_up(ob):
    """Function to boot up the gui for the different worlds

    Args:
        ob ([list]): [list of obstacles to initialise them in the gui]
    """
    global position_x, position_y
    position_x = 0
    position_y = 0
    robot.penup()
    robot.goto(100,200)
    robot.pendown()
    for i in range(2):
        robot.rt(90)
        robot.fd(400)
        robot.rt(90)
        robot.fd(200)
    robot.lt(90)
    for i in range(len(ob)):
        robot.penup()
        robot.goto(ob[i][0],ob[i][1])
        robot.begin_fill()
        for x in range(4):
            robot.pendown()
            robot.fd(4)
            robot.rt(90)
        robot.end_fill()
        robot.penup()

    robot.penup()
    robot.goto(0,0)
    


def show_position(robot_name, directions):
    """
    displays the robots position
    also alters the turtle arrows postion in regards to left right back and forward
    """
    global previous_direction
    if previous_direction == 'forward' and directions == 'right':
        robot.rt(90)
        previous_direction = directions
    elif previous_direction == 'forward' and directions == 'left':
        robot.lt(90)
        previous_direction = directions
    elif previous_direction == 'back' and directions == 'left':
        robot.rt(90)
        previous_direction = directions
    elif previous_direction == 'back' and directions == 'right':
        robot.lt(90)
        previous_direction = directions
    elif previous_direction == 'right' and directions == 'back':
        robot.rt(90)
        previous_direction = directions
    elif previous_direction == 'right' and directions == 'forward':
        robot.lt(90)
        previous_direction = directions
    elif previous_direction == 'left' and directions == 'forward':
        robot.rt(90)
        previous_direction = directions
    elif previous_direction == 'left' and directions == 'back':
        robot.lt(90)
        previous_direction = directions
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
    path = world.obstacles.is_position_blocked(new_x, new_y)
    position = world.obstacles.is_path_blocked(position_x, position_y, new_x, new_y)
    if path != True and position != True:
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
        robot.goto(new_x,new_y)
        return True, ''
    return False, 'boundary'