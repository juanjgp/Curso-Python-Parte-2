import os
import readchar
import random

# Const
POS_X = 0
POS_Y = 1


obstacle_definition = """\
#########         
#########         
#########         
              ####
              ####\
"""

# Initial position
my_position = [3, 3]

# Cola snake
tail_lenght = 0
tail = []

# Objects
repeat = 1
object =[]
map_objects = []

# Create obstacle map

obstacle_definition = [list(row) for row in obstacle_definition.split(("\n"))]
print(obstacle_definition)
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

while repeat < 11:
    object = [random.randint(1, 14) for _ in range(2)]
    repeat += 1
    map_objects.append(object)

objects = len(map_objects)

while True:
    # Draw Map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):

            char_to_draw = " "

            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = "*"

            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_draw = "@"

                if my_position in tail:
                    print("Fin del juego")
                    tail = []
                    break

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"

            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "#"


            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")


    #print("la cola {}".format(tail))
    print(my_position)
    #print(map_objects)
    #print(tail_lenght)

    # Ask user where he wants to move
    # direction = input("¿Donde te quieres mover? [WASD]: ")
    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        break

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_lenght]
            my_position = new_position

    for i in range(objects):
        if my_position == map_objects[i]:
            object = [random.randint(1, 14) for _ in range(2)]
            print(object)
            map_objects[i] = object
            tail_lenght += 1



    os.system("cls")




    # Al llegar al borde, vuelve al otro lado. MI SOLUCIÓN
    # if my_position[POS_X] > MAP_WIDTH - 1:
    # my_position[POS_X] = 0
    # elif my_position[POS_X] < 0:
    # my_position[POS_X] = MAP_WIDTH - 1
    # elif my_position[POS_Y] > MAP_HEIGHT - 1:
    # my_position[POS_Y] = 0
    # elif my_position[POS_Y] < 0:
    # my_position[POS_Y] = MAP_HEIGHT - 1
    # print(my_position)
