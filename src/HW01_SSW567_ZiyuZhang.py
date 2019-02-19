# @ZiyuZhang SSW567 HW1
import unittest
from collections import defaultdict


class triangle():
    __solts__ = {}

    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.typedict = defaultdict(int)

    def type(self):
        if not self.is_triangle():
            return
        if self.is_equilateral():
            self.typedict["equilateral"] = 1
        if self.is_isosceles():
            self.typedict["isosceles"] = 1
        if self.is_scalene():
            self.typedict["scalene"] = 1
        if self.is_right():
            self.typedict["right"] = 1

    def is_triangle(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            return False

    def is_equilateral(self):
        return (self.a == self.b == self.c)

    def is_isosceles(self):
        if self.a == self.b:
            return True
        if self.a == self.c:
            return True
        if self.b == self.c:
            return True
        return False

    def is_scalene(self):
        return (not self.is_equilateral() and not self.is_isosceles())

    def is_right(self):
        if self.a > self.b:
            if self.a > self.c:
                return self.a * self.a == self.b * self.b + self.c * self.c
        elif self.b > self.c:
                return self.b * self.b == self.a * self.a + self. c * self.c

        return self.c * self.c == self.a * self.a + self.b * self.b

    def classify(self):
        # This part troubles me a lot
        # Initially, I cannot deal with those triangles with multiple characters.
        result = str()
        self.type()
        for name, value in self.typedict.items():
            if value == 1:
                result += ("This is a(n) {} triangle. ".format(name))

        if result == "":
            result = "This is not a triangle. "
        return result


class TestTriangle(unittest.TestCase):
    def test_triangle(self):
        right_tri = triangle(3, 4, 5)
        iso_tri = triangle(2, 2, 3)
        equ_tri = triangle(1, 1, 1)
        sca_tri = triangle(3, 4, 6)
        not_tri = triangle(3, 4, 1)
        self.assertEqual(right_tri.classify(), "This is a(n) scalene triangle. This is a(n) right triangle. ")
        self.assertEqual(iso_tri.classify(), "This is a(n) isosceles triangle. ")
        self.assertEqual(equ_tri.classify(), "This is a(n) equilateral triangle. This is a(n) isosceles triangle. ")
        self.assertEqual(sca_tri.classify(), "This is a(n) scalene triangle. ")
        self.assertEqual(not_tri.classify(), "This is not a triangle. ")


def main():
    right_tri = triangle(3, 4, 5)
    print(right_tri.classify())


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
    main()
