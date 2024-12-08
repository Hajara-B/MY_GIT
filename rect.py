
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return (self.length * self.breadth)
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def compare_area(self, other):
        if self.area() > other.area():
            return 
        elif self.area() < other.area():
            return
        else:
            return 
rect1 = Rectangle(10, 5)
rect2 = Rectangle(8, 6)
print(f"Rectangle 1: Area = {rect1.area()}, Perimeter = {rect1.perimeter()}")
print(f"Rectangle 2: Area = {rect2.area()}, Perimeter = {rect2.perimeter()}")
comparison_result = rect1.compare_area(rect2)
print(comparison_result)
