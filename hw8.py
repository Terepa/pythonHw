class Rectangle():

    def __init__(self, l, w):

        self.length = l

        self.width  = w

    def area(self):

        return self.length*self.width

new_rectangle = Rectangle(5, 6)

new_rectangle.length = 7

print(new_rectangle.area())