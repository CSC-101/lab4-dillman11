import math

import data
from data import Point


# Write your functions for each part in the space below.

# Part 1
def first_element(list1: list) -> list:
    list2 = []
    for first in list1:
        if isinstance(first, list):
            if first != []:
                list2.append(first[0])
    return list2

# Part 2
def x_coordinates(points: list) -> list:
    all_x_coordinates = []
    for point in points:
        all_x_coordinates.append(point.x)
    return all_x_coordinates

# Part 3
def are_in_positive_quadrant(points: list) -> list:
    positive_quadrant_list = []
    for point in points:
        if point.x == abs(point.x) and point.y == abs(point.y):
            positive_quadrant_list.append(point)
    return positive_quadrant_list


# Part 4
def distance(point1: Point, point2: Point) -> float:
    return round(float(math.sqrt(pow((point2.x-point1.x),2) + pow((point2.y-point1.y),2))),2)


# Part 5
def manhattan_distance(point1: Point, point2: Point) -> float:
    return float(abs(point1.x-point2.x)+abs(point1.y-point2.y))

# Part 6
def distance_all(points: list):
    distances = []
    origin = data.Point(0, 0)
    for point in points:
        distances.append(manhattan_distance(point, origin))
    return distances