# Every function receive coordinates of two grid points returns estimated distance between them.
# Each argument is a tuple of two or three integer coordinates.

import math

def grid_2D_heuristic(current, destination):
    return abs(current[0] - destination[0]) + abs(current[1] - destination[1])

def grid_diagonal_2D_heuristic(current, destination):
    return max(abs(current[0] - destination[0]), abs(current[1] - destination[1]))

def grid_3D_heuristic(current, destination):
    return abs(current[0] - destination[0]) + abs(current[1] - destination[1]) + abs(current[2] - destination[2])

def grid_face_diagonal_3D_heuristic(current, destination):
    x = abs(current[0] - destination[0])
    y = abs(current[1] - destination[1])
    z = abs(current[2] - destination[2])
    return math.ceil(max(x, y, z, (x + y + z) / 2))

def grid_all_diagonal_3D_heuristic(current, destination):
    return max(abs(current[0] - destination[0]), abs(current[1] - destination[1]), abs(current[2] - destination[2]))

def grid_knight_2D_heuristic(current, destination):
    x = abs(current[0] - destination[0])
    y = abs(current[1] - destination[1])
    return math.ceil(max(x / 2, y / 2, (x + y) / 3))
