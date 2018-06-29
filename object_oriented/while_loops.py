a = 0
b = 8

while a < 4:
    print("-------------------")
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print("{0} / {1} cannot be divided by zero".format(a, b))
        break
    finally:
        print("{0} / {1} This will always run".format(a, b))

    print("You are out of the exception and on the main loop")

else:
    print("Code executed without a zero division")
