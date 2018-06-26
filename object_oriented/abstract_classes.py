import abc


class GetterSetter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, input):
        """Set a value in the instance """
        return

    @abc.abstractmethod
    def get_val(self):
      """Get and return a value from the instance"""
      return


class MyClass(GetterSetter):

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val


a = MyClass()
print(a)
