# -*- coding: utf-8 -*-
"""
Updated Oct 27, 2025
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: jg
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Right triangles
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
    
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4,3,5),'Right')

    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(8,15,17),'Right')

    def testRightTriangleE(self):
        self.assertEqual(classifyTriangle(7,24,25),'Right')

    # Equilateral triangles
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral')

    def testEquilateralTrianglesC(self):
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral')

    # Isosceles triangles
    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(5,5,8),'Isosceles')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(3,5,5),'Isosceles')

    def testIsoscelesTriangleC(self): 
        self.assertEqual(classifyTriangle(10,10,15),'Isosceles')

    def testIsoscelesTriangleD(self):
        self.assertEqual(classifyTriangle(7,11,7),'Isosceles')

    # Scalene triangles
    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(4,5,6),'Scalene')
    
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(10,11,12),'Scalene')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(5,6,7),'Scalene')

    # Not a triangle
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle')
    
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(5,1,2),'NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(1,10,12),'NotATriangle')

    # Invalid inputs
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1,5,6),'InvalidInput')
    
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(201,5,6),'InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(5,300,6),'InvalidInput')

    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(5,6,0),'InvalidInput')

    def testInvalidInputE(self):
        self.assertEqual(classifyTriangle(5.5,6,7),'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

