class Triangle:
    """Triangle class"""
    side_quantity = 3
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    

    def area(self):
        perimeter = (self.a + self.b + self.c)
        s = perimeter / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area


triangulos = [
    Triangle(3, 4, 5),
    Triangle(5, 12, 13),
    Triangle(8, 15, 17),
    Triangle(12, 35, 37)
]

for t in triangulos:
    print(f"Area of triangle is: {t.area()}")