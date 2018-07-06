from fractions import Fraction
import math

print(Fraction(0.125))
# should be 1/8

print(Fraction('0.125'))
# python recognizes is a fraction and transforms it to 1/8

x = Fraction(math.pi)

print("Pi respresentation in a fraction {0}".format(x))
print("The aproximations of pi in a float is {0}".format(float(x)))


# We can limit the denomitar by using the following function
print(x.limit_denominator(10))
print("The float would be {0}".format(float(x.limit_denominator(10))))

