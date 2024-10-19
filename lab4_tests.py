import math

import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[1,2,3],4,[5,6,7],[8,9,10,11],[]]
        result = lab4.first_element(input)
        expected = [1,5,8]
        self.assertEqual(expected, result)


    # Part 2
    def test_x_coordinates_1(self):
        input = [data.Point(2,3), data.Point(5,9), data.Point(7,10)]
        result = lab4.x_coordinates(input)
        expected = [2,5,7]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input = [data.Point(9,5), data.Point(15,29), data.Point(3,6)]
        result = lab4.x_coordinates(input)
        expected = [9,15,3]
        self.assertEqual(expected, result)


    # Part 3
    def test_are_in_positive_quadrant_1(self):
        input = [data.Point(2,5), data.Point(-8, 3), data.Point(7,2), data.Point(6,-9)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(2,5), data.Point(7,2)]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        input = [data.Point(-5,9),data.Point(6,3),data.Point(3,-6),data.Point(1262, 682)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(6,3), data.Point(1262,682)]
        self.assertEqual(expected, result)

    # Part 4
    def test_distance_1(self):
        input1 = data.Point(5,10)
        input2 = data.Point(15,30)
        result = lab4.distance(input1, input2)
        expected = 22.36
        self.assertEqual(expected, result)

    def test_distance_2(self):
        input1 = data.Point(16,8)
        input2 = data.Point(-5,53)
        result = lab4.distance(input1, input2)
        expected = 49.66
        self.assertEqual(expected, result)

    # Part 5
    def test_manhattan_distance_1(self):
        input1 = data.Point(7,16)
        input2 = data.Point(20,-2)
        result = lab4.manhattan_distance(input1, input2)
        expected = 31
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        input1 = data.Point(13,9)
        input2 = data.Point(-12,43.5)
        result = lab4.manhattan_distance(input1, input2)
        expected = 59.5
        self.assertEqual(expected, result)


    # Part 6
    def test_distance_all(self):
        input = [data.Point(5,12), data.Point(34,-62), data.Point(-14, 35)]
        result = lab4.distance_all(input)
        expected = [17, 96, 49]
        self.assertEqual(expected, result)

    def test_distance_all(self):
        input = [data.Point(43.7, 6), data.Point(-53.67, 105.2), data.Point(.5, -.6)]
        result = lab4.distance_all(input)
        expected = [49.7, 158.87, 1.1]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
