# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2
# ¡­ The numbers after the direction are steps. Please write a program to compute the
# distance from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer. Example:
# If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2
# Then, the output of the program should be: 2

import math

print("Input movement commands: ", end="")
user_input = input()
directions = []
for x in range(0, len(user_input.split(" "))):
    if x%2!=0:
        directions.append(user_input.split(" ")[x])

horizontal_movement = int(directions[2]) - int(directions[3])
if horizontal_movement<0:
    horizontal_movement = horizontal_movement * -1

vertical_movement = int(directions[0]) - int(directions[1])
if vertical_movement<0:
    vertical_movement = vertical_movement * -1

distance = math.sqrt(horizontal_movement*horizontal_movement + vertical_movement*vertical_movement)
print(distance)