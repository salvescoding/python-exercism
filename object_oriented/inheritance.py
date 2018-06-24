class Animal(object):
    def __init__(self, name):
        self.name = name

    def high_level(self):
        return "This is a high level function"


class Run(object):
    def high_level(self):
        return "Run fast!"


class Dog(Animal):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def bark(self):
        return "Woof Woof madafuckker!"


class DogType(Dog, Run):

      def __init__(self, name, color, type):
          super().__init__(name, color)
          self.type = type


dt = DogType("Brami", "Blonde", "Labrador")
print(dt.high_level())
print(DogType.mro())
print(dt.name, dt.color, dt.type)
