import math

class Point:
    x = 0
    y = 0
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y    

class Triangle:

    #Input is the three points of a triangle
    def __init__(self, a: Point, b: Point, c: Point):
        #Set the points
        self._a = a
        self._b = b
        self._c = c

    #Calc the distances between point A and point B
    def distance_between_a_and_b(self):
        return math.sqrt(math.pow(self._a.x - self._b.x, 2) + math.pow(self._a.y - self._b.y, 2))
    
    #Calc the distances between point B and point C
    def distance_between_b_and_c(self):
        return math.sqrt(math.pow(self._b.x - self._c.x, 2) + math.pow(self._b.y - self._c.y, 2))
    
    #Calc the distances between point A and point C
    def distance_between_a_and_c(self):
        return math.sqrt(math.pow(self._b.x - self._a.x, 2) + math.pow(self._b.y - self._a.y, 2))
    
    def is_valid_triangle(self) -> bool:
        if self.distance_between_a_and_b() + self.distance_between_a_and_c() <= self.distance_between_b_and_c():
            return False
        if self.distance_between_a_and_b() + self.distance_between_b_and_c <= self.distance_between_a_and_c():
            return False
        if self.distance_between_b_and_c() + self.distance_between_a_and_c() <= self.distance_between_a_and_b():
            return False
        return True

    def is_right(self) -> bool:
        #First get the side lengths
        ab = math.sqrt(math.pow(self._a.x - self._b.x, 2) + math.pow(self._a.y - self._b.y, 2))
        bc = math.sqrt(math.pow(self._b.x - self._c.x, 2) + math.pow(self._b.y - self._c.y, 2))
        ac = math.sqrt(math.pow(self._b.x - self._a.x, 2) + math.pow(self._b.y - self._a.y, 2))

        side_1 = 0
        side_2 = 0
        hypot = 0

        #Now find the hypot
        if ab > bc and ab > ac:
            side_1 = bc
            side_2 = ac
            hypot = ab
        if ac > ab and ac > bc:
            side_1 = ab
            side_2 = bc
            hypot = ac
        else:
            side_1 = ac
            side_2 = ab
            hypot = bc

        #Pythangorean theorem! leg_1^2 + leg_2^2 = hypot^2
        return math.pow(side_1, 2) + math.pow(side_2, 2) == math.pow(hypot, 2)
    
    def is_equialateral(self) -> bool:
        return self._ab == self.bc == self._ac

    def calc_area(self) -> int:
        #use heron's forumla
        return  math.sqrt(s * (s - self._ab) * (s - self._ac) * (s - self._bc))
    
    def calc_perimeter(self):
        return self._ab + self._bc + self._ac


triangle_1 = Triangle(Point(0,0), Point(0,3), Point(4,0))
print(triangle_1.is_right())
print(triangle_1.is_valid_triangle())
print(triangle_1.calc_area())
print(triangle_1.calc_perimeter())

triangle_2 = Triangle(Point(0,0), Point(0,2), Point(1,1))
print(triangle_2.is_right())
print(triangle_2.is_valid_triangle())
print(triangle_2.calc_area())
print(triangle_2.calc_perimeter())
