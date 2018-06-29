# For loops are used for iterables, like strings, tuples, lists, dict
# Normal for loop

s = "Hello"
t = ("Hi", "How", "Are")
for i in s:
  print(i)

for i in t:
  print(i)

# Iterate through a list of tuples
for i, j in [("John", 23), ("Ser", 34)]:
    print(i, j)

# Iterate with the index
for i, el in enumerate(s):
    print("Index {0} belongs to element {1}".format(i, el))

