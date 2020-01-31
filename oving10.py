import math
from random import random, seed


class Circle(object):   # Inherits from object
    'An advanced circle analytic toolkit'

    # Flyweight design pattern suppresses
    # The instance dictionary
    __slots_ = ['diameter']

    version = '0.1'

    def __init__(self, radius):
        self.radius = radius  # instance variable

    @classmethod    # Alternative constructor
    def from_bbd(cls, bbd):
        'Construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @property   # Converted dotted access to method calls
    def radius(self):
        'Radius of circle'
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        'Setting the diameter'
        self.diameter = radius * 2.0

    def area(self):
        p = self.__perimeter()  # Class local reference
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @staticmethod   # Attach function to all classes
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0


class Tire(Circle):
    'Tires are circles with an odometer corrected perimeter'

    def perimeter(self):
        'Circumference corrected for the rubber'
        return _Tire_.perimeter(self) * 1.25


# Tutorial 1
print('Circuitous version', Circle.version)
c = Circle(10)
print('A circle of radius', c.radius)
print('has an area of', c.area())

# First customer: Academia
seed(8675309)
print('Using Circuitous(tm) version', Circle.version)
n = 10
circles = [Circle(random()) for i in range(n)]
print('The average area of', n, 'random circles')
avg = sum([c.area() for c in circles]) / n
print('is %.1f' % avg)
print()

# Second customer: Rubber sheet company
cuts = [0.1, 0.7, 0.8]
circles = [Circle(r) for r in cuts]
for c in circles:
    print('A circle with a radius of', c.radius)
    print('has a perimeter of', c.perimeter())
    print('and a cold area of', c.area())
    c.radius *= 1.1
    print('and a warm area of', c.area())
print()


# Third customer: National tire chain
t = Tire(22)
print('A tire of radius', t.radius)
print('has an inner area of', t.area())

# Tire function called first, but uses perimiter from Circle
# Extend parent and let it compute and then scale it
print('and an odometer corrected perimeter of', t.perimeter())
print()

# Fourth customer: National graphics company
bbd = 25.1
c = Circle.from_bbd(bbd)
print('A circle with a bbd of 25.1')
print('has a radius of', c.radius)
print('an area of', c.area())
print()

# User request: Many circles
n = 10000000
seed(8675309)
print('Circuitous version', Circle.version)
circles = [Circle(random()) for i in range(n)]
print('The average area of', n, 'random circles')
avg = sum([c.area() for c in circles]) / n
print('is %.1f' % avg)
