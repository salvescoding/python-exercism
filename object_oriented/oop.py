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


a = MaxSizeList(3)
b = MaxSizeList(2)

a.push("hello")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hello")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
