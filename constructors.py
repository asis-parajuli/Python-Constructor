class Point:
    # The method that we define in a class should have atleast one parameter which by convention is called self
    def __init__(self, x, y):  # self is a reference to the current point object
        self.x = x
        self.y = y
        # Two attributes for our point object in the constructor of the Point class

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
# what if we want to supply initial value x and y to our object point like point = Point(1, 2)
# for this purpose we need constructor which is a special is a special method which is called when we create a new point object
point.draw()
