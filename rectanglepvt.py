class Rectangle:
    def __init__(self, length, width):

        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def area(self):
        return self.__length * self.__width

    
    def __lt__(self, other):
     
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return False


    def display(self):
        print(f"Rectangle: Length = {self.__length}, Width = {self.__width}, Area = {self.area()}")

print("Enter details for Rectangle 1:")
length1 = float(input("Enter length of Rectangle 1: "))
width1 = float(input("Enter width of Rectangle 1: "))

print("\nEnter details for Rectangle 2:")
length2 = float(input("Enter length of Rectangle 2: "))
width2 = float(input("Enter width of Rectangle 2: "))

rect1 = Rectangle(length1, width1)
rect2 = Rectangle(length2, width2)


print("\nDetails of Rectangle 1:")
rect1.display()
print("\nDetails of Rectangle 2:")
rect2.display()

if rect1 < rect2:
    print("\nRectangle 1 has a smaller area than Rectangle 2.")
elif rect1 > rect2:
    print("\nRectangle 1 has a larger area than Rectangle 2.")
else:
    print("\nBoth rectangles have the same area.")
