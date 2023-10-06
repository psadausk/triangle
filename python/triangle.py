import math

class Point:
    x = 0
    y = 0
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
    

class Triangle:

    #Input is the three points of a triangle
    def __init__(self, a: Point, b: Point, c: Point):\
        #Set the points
        self._a = a
        self._b = b
        self._c = c

        #set the side lengths. Makes it easier to calc things
        self._ab = math.sqrt(math.pow(self._a.x - self._b.x, 2) + math.pow(self._a.y - self._b.y, 2))
        self._ac = math.sqrt(math.pow(self._a.x - self._c.x, 2) + math.pow(self._a.y - self._c.y, 2))
        self._bc = math.sqrt(math.pow(self._b.x - self._c.x, 2) + math.pow(self._b.y - self._c.y, 2))

        print(self._ab, self._bc, self._ac)
    
    #Note given the setup this is always true
    def is_valid_triangle(self) -> bool:
        if self._ab + self._ac <= self._bc:
            return False
        if self._ab + self._bc <= self._ab:
            return False
        if self._bc + self._ac <= self._ab:
            return False
        return True

    def is_right_triangle(self) -> bool:
        #determine the legs.Longest side is the hypotenuse
        sides = [self._ab, self._bc, self._ac]

        sides.sort()

        leg_1 = sides[0]
        leg_2 = sides[1]
        hypot = sides[2]

        #Pythangorean theorem! leg_1^2 + leg_2^2 = hypot^2
        return math.pow(leg_1, 2) + math.pow(leg_2, 2) == math.pow(hypot, 2)
    
    def is_equialateral(self) -> bool:
        return self._ab == self.bc == self._ac

    def calc_area(self) -> int:
        #use heron's forumla
        s = .5 * (self._ab + self._bc + self._ac)
        return  math.sqrt(s * (s - self._ab) * (s - self._ac) * (s - self._bc))
    
    def calc_perimeter(self):
        return self._ab + self._bc + self._ac


triangle_1 = Triangle(Point(0,0), Point(0,3), Point(4,0))
print(triangle_1.is_right_triangle())
print(triangle_1.is_valid_triangle())
print(triangle_1.calc_area())
print(triangle_1.calc_perimeter())

triangle_2 = Triangle(Point(0,0), Point(0,2), Point(1,1))
print(triangle_2.is_right_triangle())
print(triangle_2.is_valid_triangle())
print(triangle_2.calc_area())
print(triangle_2.calc_perimeter())
