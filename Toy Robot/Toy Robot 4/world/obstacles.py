import random
obstacles_list = []

def get_obstacles():
    """Generate a number of obstacles between 0 and 10 then randomly generate their postion between my boundaries
    check if the obstacles are at start or inside of each other and if they are then remake them
    """
    global obstacles_list
    obstacles_number = 0
    obstacles_list = []
    obstacles_tuple = ()
    obstacles_number = random.randint(1,10)
    for x in range(obstacles_number):
        obstacles_tuple = (random.randint(-100,100), random.randint(-200,200))
        if obstacles_tuple[0] == 0 or obstacles_tuple[1] == 0:
            obstacles_tuple = (random.randint(-100,100), random.randint(-200,200))
        elif obstacles_tuple in obstacles_list:
            obstacles_tuple = (random.randint(-100,100), random.randint(-200,200))
        else:
            obstacles_list.append(obstacles_tuple)
    obstacles_number = 0
    return(obstacles_list)


def obstacles_position_list(i):
    """Function to generate all the possible x y co-ordinates of each obstacle passed to it

    Args:
        i ([tuple]): [a tuple of (x,y) co-ordinates that are the start of an obstacle]

    Returns:
        [list]: [list of all possible (x,y) co-ordinates of an obstacle]
    """
    obstacles_tuple_list = []
    for x in range(i[0], i[0]+5):
        for y in range(i[1], i[1]+5):
            obstacle_tuple = x,y
            obstacles_tuple_list.append(obstacle_tuple)
    return obstacles_tuple_list


def is_position_blocked(x,y):
    """Runs a list of obstacles through a function and takes it return of a list and appends them to a 
    larger list of co-orddinates for each obstacle. After that it runs through the list and checks 
    if my postion tuple made of my (x,y) co-ordiante passed to it is in the list and returns True if it 
    is and false if not

    Args:
        x ([int]): [x - co-ordinate]
        y ([int]): [y - co-ordinate]

    Returns:
        [boolean]: [Ture if obstacle at postion x,y False if not]
    """
    coordinate_tuple = x,y
    list_portion = []
    final_list = []
    for i in obstacles_list:
        list_portion = obstacles_position_list(i)
        final_list += list_portion
        #print(final_list)
    for i in final_list:
        if coordinate_tuple == i:
            return True
    return False

def is_path_blocked(x1,y1, x2, y2):
    """[summary]

    Args:
        x1 ([type]): [description]
        y1 ([type]): [description]
        x2 ([type]): [description]
        y2 ([type]): [description]

    Returns:
        [type]: [description]
    """
    path_list = []
    path_tuple = ()
    x_list = []
    y_list = []
    x_step = 1
    y_step = 1
    if x1 > x2:
        x_step = -1
    if y1 > y2:
        y_step = -1
    if x1 == x2:
        for y in range (y1,y2,y_step):
            path_tuple = (x1,y)
            path_list.append(path_tuple)
    elif y1 == y2:
        for x in range(x1,x2,x_step):
            path_tuple = (x,y1)
            path_list.append(path_tuple)
    # else:
    #     for x in range(x1,x2,x_step):
    #         x_list.append(x)
    #     for y in range(y1,y2,y_step):
    #         y_list.append(y)
    #     path_list.append(list(zip(x_list,y_list)))

    for i in path_list:
        if is_position_blocked(i[0],i[1]) == True:
            return True
    return False
