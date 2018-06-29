import ctypes


class MaxSizeList:
    def __init__(self, max_size):
        self.max_size = max_size
        self.new_list = []

    def push(self, arg):
        self.new_list.append(arg)
        if len(self.new_list) > self.max_size:
            self.new_list.pop(0)

    def get_list(self):
        return self.new_list


class Rectangle():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("height must be positive")
        else:
            self._height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    # Check the equality between 2 rectangles instances based on width and height
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    # check if the object is less than other object based on area() in this case
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

    # Representation special method to output the object the way we would like to
    def __repr__(self):
        return "Rectangle width: {0}, height: {1}".format(self.width, self.height)


r1 = Rectangle(5, 20)
r1.width = 10
print(r1.area())
print(r1.perimeter())
print(hex(id(r1)))


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


a = [1, 2, 3]
# b = a
# print(id(a))
# print(id(b))
# print(ref_count(id(a)))


# r2 = Rectangle(20, 40)
# r2.height = 60
# print(r2.area())
# print(r1 is r2)
# print(r1 == r2)
# print(r1 == 100)
# print(r1 < r2)

# a = MaxSizeList(3)
# b = MaxSizeList(2)

# a.push("hello")
# a.push("hi")
# a.push("let's")
# a.push("go")

# b.push("hello")
# b.push("hi")
# b.push("let's")
# b.push("go")

# print(a.get_list())
# print(b.get_list())
