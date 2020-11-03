

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ")
    if shape.lower() == "pyramid":
        return shape.lower()
    elif shape.lower() == "triangle":
        return shape.lower()
    elif shape.lower() == "square":
        return shape.lower()
    else:
        return get_shape()



# TODO: Step 1 - get height (it must be int!)
def get_height():
    h = input("Height?: ")
    if h.isdigit() == True:
        height = int(h)
    else:
        return get_height()
    if height > 0 and height < 81:
        return height
    else:
       return get_height()

# TODO: Step 2
def draw_pyramid(height, outline):
   if outline == 0:
        i = height - 1
        for j in range (1, height * 2, 2):
            print (" " * i+j * "*")
            i = i - 1
   else:
        n = 0
        for row in range(1, height + 1):
            for col in range (height - row):
                print(end = " ")
            while n!= (2 * row - 1):
                if n == 0 or n == (2 * row -1)-1 or row == height:
                    print("*", end = "")
                else:
                    print (end = " ")
                n = n + 1
            n = 0
            print()

    


# TODO: Step 3
def draw_square(height, outline):

    x = height
    if outline == 0:
        for i in range(1, height+1):
            print("*" * height)
    else:
        for row in range(1, x+1) : 
            for col in range(1, x+1) : 
                if (row == 1 or row == x or 
                    col == 1 or col == x) :             
                    print("*", end = "")             
                else : 
                    print(" ", end = "")             
          
            print() 


# TODO: Step 4
def draw_triangle(height, outline):
    
    i = 0
    base = 1
    if outline == 0:
        for i in range(1, height + 1):
            e = ( "*") * i
            print (e)
    else:
        while i < height:
            for k in range(base):
                if i == 0 or i == height - 1 or k == 0 or k == base-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            base = base + 1
            i = i + 1
            print()
        

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    answer = input("Outline only? (y/N)")
    if answer == "Y":
        return(1)
    else:
        return(0)
    


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

