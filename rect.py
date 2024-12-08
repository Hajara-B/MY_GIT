
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
            return "1st rectangle has larger area"
        elif self.area() < other.area():
            return "2nd rectangle has larger area"
        else:
            return "both have same area"
length1 = float(input("Enter the length of the first rectangle: "))
breadth1 = float(input("Enter the breadth of the first rectangle: "))
length2 = float(input("Enter the length of the second rectangle: "))
breadth2 = float(input("Enter the breadth of the second rectangle: "))


rect1 = Rectangle(length1, breadth1)
rect2 = Rectangle(length2, breadth2)

     
print(f"Rectangle 1: Area = {rect1.area()}, Perimeter = {rect1.perimeter()}")
print(f"Rectangle 2: Area = {rect2.area()}, Perimeter = {rect2.perimeter()}")
comparison_result = rect1.compare_area(rect2)
print(comparison_result)

