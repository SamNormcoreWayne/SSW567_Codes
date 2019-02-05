# -*- coding: utf-8 -*-
"""
The objective of this assignment is for you to
(a) develop a set of tests for an existing triangle classification program,
(b) use those tests to find and fix defects in that program,
and (c) report on your testing results for the Triangle problem

Updated Feb 8, 2019
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: Ziyu Zhang

I have never copied code from classmates or from the Internet.
All the codes are finished by myself except for the sentences you giving on Canvas
"""

import unittest

from Triangle_Modified_Ziyu import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    # Modifying is from here.

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a triangle.')

    def testNotTriangleB(self):
        self.assertEqual(classifyTriangle(3, 5, 10), 'NotATriangle', '3,5,10 is not a triangle.')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene', '3, 3, 4 is a scalene triangle. ')

    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isoceles', '7 ,8 ,9 is a isoceles triangle. ')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

